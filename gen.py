import json
import os
from pathlib import Path
from typing import List, NamedTuple


def python_type(typ):
    return {
        'string': 'str',
        'integer': 'int',
        'number': 'float',
        'boolean': 'bool',
        'object': 'Any',
        'array': 'List[Any]',
    }[typ]


class Parameter(NamedTuple):
    name: str
    required: bool
    type: str

    def __str__(self):
        if self.required:
            return f"{self.name}: {self.type}"
        return f"{self.name}: Optional[{python_type(self.type)}] = None"


class RawPathKey(NamedTuple):
    path: str
    name: str
    is_get: bool

    @classmethod
    def from_path(cls, path):
        if path.endswith('s/{id}/'):
            return cls(path, path[:-len('s/{id}/')], True)
        return cls(path, path.rstrip('/'), False)


class PathKey(NamedTuple):
    path: str
    name: str
    has_get: bool

    @classmethod
    def from_raw_path(cls, raw_path: RawPathKey, has_get: bool):
        return cls(raw_path.path, raw_path.name, has_get)

    @property
    def attr_name(self):
        return self.name.replace('-', '_').replace('/', '_')

    @property
    def class_name(self):
        return self.name.replace('-', '_').replace('/', '_').capitalize() + 'Endpoint'

    @property
    def is_detailed(self):
        return '/{id}/' in self.name





def visit_prefix(prefix, data):

    header = """
from typing import Any, Dict, List, Optional, Union, Iterable
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import RecordSet, Record
from pynetbox._gen import definitions

"""

    app_cls = f"""class {prefix.capitalize()}App(App):
    def __init__(self, api: 'Api', name):
"""

    raw_path_keys = [RawPathKey.from_path(path) for path in data.keys()]
    gets = {p.name: p for p in raw_path_keys if p.is_get}
    path_keys = [PathKey.from_raw_path(k, k.name in gets) for k in raw_path_keys if not k.is_get]
    non_detailed = [p for p in path_keys if not p.is_detailed]

    keys = [f'        self.{k.attr_name}: {k.class_name} = ...' for k in non_detailed]

    def get_get_data(key: PathKey):
        g = gets.get(key.name)
        if g is not None:
            return data[g.path]

    endpoint_classes = [visit_endpoint(k, data[k.path], get_get_data(k)) for k in non_detailed]



    with open(f'pynetbox-stubs/_gen/{prefix}.pyi', 'w') as f:
        f.write(header)
        f.write('\n'.join(endpoint_classes))
        f.write(app_cls)
        f.write('\n'.join(keys))


def visit_endpoint(key: PathKey, data, get_data):
    get_params = visit_get(data['get']) if 'get' in data else []
    get_str = ', '.join(str(p) for p in get_params)

    response_type_ref = get_response_type_ref(data)
    response_type = 'definitions.' + response_type_ref[len('#/definitions/'):] if response_type_ref else 'Record'

    cls = f"""class {key.class_name}(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[{response_type}]: ...
    def get(self, {get_str}) -> Optional[{response_type}]: ...
    def filter(self, {get_str}) -> RecordSet[{response_type}]: ...
    def create(self, {get_str}) -> {response_type}: ...
    def update(self, objects: Iterable[{response_type}]) -> [{response_type}]: ...
    def delete(self, objects: Iterable[{response_type}]): ...
    def choices(self) -> dict:...
    def count(self, {get_str}) -> int: ...

"""

    return cls

def get_response_type_ref(data):
    if 'get' in data:
        _200 = data['get']['responses']['200']
        if 'schema' in _200:
            schema = data['get']['responses']['200']['schema']
            if 'properties' in schema:
                return schema['properties']['results']['items']['$ref']
            elif '$ref' in schema:
                return schema['$ref']
            assert False, schema
        elif _200 == {'description': ''}:
            return None
        assert False, _200
    return None


def visit_get(data) -> List[Parameter]:
    parameters = data['parameters']
    return [Parameter(p['name'], p['required'], p['type']) for p in parameters]


def visit_definitions(definitions: dict):
    defs = [visit_definition(k, d) for k,d in definitions.items()]

    header = """
from typing import Any, Dict, List, Optional, Union, Iterable
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import RecordSet, Record
"""

    with open('pynetbox-stubs/_gen/definitions.pyi', 'w') as f:
        f.write(header)
        f.write('\n'.join(defs))


class Property(NamedTuple):
    name: str
    type: str
    ref: str = ''

    def __str__(self):
        if self.type:
            return f"{self.name}: {python_type(self.type)}"
        if '#/definitions/' in self.ref:
            return f"{self.name}: '{self.ref[len('#/definitions/'):]}'"
        assert False, f"{self.ref}"

    @classmethod
    def from_definition(cls, name, defi):
        return cls(name, defi.get('type'), defi.get('$ref'))


def visit_definition(key, data):
    properties = [Property.from_definition(name=k, defi=data['properties'][k]) for k in data['properties']]
    properties_str = '\n'.join('        self.' + str(p) for p in properties)
    header = f"""class {key}(Record):
    def __init__(self):
{properties_str}
"""
    return header


def main():
    with open('openapi.json', 'r') as f:
        openapi = json.load(f)
    paths = openapi['paths']
    prefixes = {p.split('/')[1] for p in paths}
    if not os.path.exists('pynetbox-stubs/_gen'):
        os.mkdir('pynetbox-stubs/_gen')

    Path('pynetbox-stubs/_gen/__init__.py').touch()

    for p in prefixes:

        data = {path[len(p + '/') + 1:]: value for path, value in paths.items() if path.startswith(f'/{p}')}
        visit_prefix(p, data)

    visit_definitions(openapi['definitions'])


if __name__ == "__main__":
    main()
