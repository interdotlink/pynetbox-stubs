import json
import os
from enum import StrEnum
from pathlib import Path
from typing import Any, Dict, List, Literal, NamedTuple, Optional, Union


class PythonType(StrEnum):
    str = "str"
    int = "int"
    float = "float"
    bool = "bool"
    any = "Any"
    list = "List[Any]"
    none = "None"
    dict = "Dict[str, Any]"

    @classmethod
    def from_json(cls, json_type: "Literal[PythonType.str]") -> "PythonType":
        return {
            "string": cls.str,
            "integer": cls.int,
            "number": cls.float,
            "boolean": cls.bool,
            "object": cls.any,
            "array": cls.list,
            "null": cls.none,
        }[json_type]


class Parameter(NamedTuple):
    name: str
    required: bool
    type: Optional[PythonType]

    @property
    def type_allow_int(self) -> Union[Optional[PythonType], str]:
        if (
            self.name == "id"
            or self.name.endswith("_id")
            or self.name == "depth"
        ) and not self.type == "int":
            return f"{self.type} | int"
        return f"{self.type}"

    def __str__(self) -> str:
        if self.name == "**kwargs":
            return f"{self.name}: Optional[{self.type_allow_int}]"
        if self.required:
            return f"{self.name}: {self.type_allow_int}"
        return f"{self.name}: Optional[{self.type_allow_int}] = None"


class ParameterList:
    def __init__(self, parameters: List[Parameter]) -> None:
        self.parameters = parameters

    def __str__(self) -> str:
        return ", ".join(
            str(p)
            for p in sorted(
                self.parameters, key=lambda p: p.required, reverse=True
            )
        )


class RawPathKey(NamedTuple):
    path: str
    name: str
    is_get: bool

    @classmethod
    def from_path(cls, path: str) -> "RawPathKey":
        if path.endswith("s/{id}/"):
            return cls(path, path[: -len("s/{id}/")], True)
        elif path.endswith("/{id}/"):
            return cls(path, path[: -len("/{id}/")], True)
        return cls(path, path.rstrip("/"), False)


class PathKey(NamedTuple):
    path: str
    name: str
    has_get: bool

    @classmethod
    def from_raw_path(cls, raw_path: RawPathKey, has_get: bool) -> "PathKey":
        return cls(raw_path.path, raw_path.name, has_get)

    @property
    def attr_name(self) -> str:
        return self.name.replace("-", "_").replace("/", "_")

    @property
    def class_name(self) -> str:
        return (
            self.name.replace("-", "_").replace("/", "_").capitalize()
            + "Endpoint"
        )

    @property
    def is_detailed(self) -> bool:
        return "/{id}/" in self.name


def visit_prefix(
    prefix: str, data: Dict[str, dict], defs: List["RecordDefinition"]
) -> None:
    header = """
from typing import Any, Dict, Iterable, List, Optional, Union, overload

from pynetbox._gen import definitions
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import Record, RecordSet


"""

    app_cls = f"""class {prefix.capitalize()}App(App):
    def __init__(self, api: 'Api', name):
"""

    raw_path_keys = [RawPathKey.from_path(path) for path in data.keys()]
    gets = {p.name: p for p in raw_path_keys if p.is_get}
    path_keys = [
        PathKey.from_raw_path(k, k.name in gets)
        for k in raw_path_keys
        if not k.is_get
    ]
    non_detailed = [p for p in path_keys if not p.is_detailed]

    keys = [
        f"        self.{k.attr_name}: {k.class_name} = ..."
        for k in non_detailed
        if k.name
    ]
    if not keys:
        keys = ["        ..."]

    def get_get_data(key: PathKey) -> Optional[dict]:
        g = gets.get(key.name)
        if g is not None:
            return data[g.path]
        return None

    endpoint_classes = [
        visit_endpoint(k, data[k.path], defs) for k in non_detailed
    ]

    with open(f"pynetbox-stubs/_gen/{prefix}.pyi", "w") as f:
        f.write(header)
        f.write("\n".join(endpoint_classes))
        f.write(app_cls)
        f.write("\n".join(keys))


def visit_endpoint(
    key: PathKey,
    data: Dict[str, dict],
    defs: List["RecordDefinition"],
) -> str:
    get_str = str(visit_get(data["get"])) if "get" in data else ""
    if get_str:
        get_str += ", " + str(
            Parameter(
                name='**kwargs',
                required=False,
                type=PythonType.any,
            )
        )

    else:
        get_str = str(
            Parameter(
                name='**kwargs',
                required=False,
                type=PythonType.any,
            )
        )

    create_str = (
        str(visit_create(data["post"], defs)) if "post" in data else ""
    )

    response_type_ref = get_response_type_ref(data)
    if response_type_ref and response_type_ref.startswith(
        "#/components/schemas/Paginated"
    ):
        for definition in defs:
            if (
                definition.name
                == response_type_ref[len("#/components/schemas/") :]
            ):
                response_type_ref = definition.properties[-1].ref
                break
        else:
            assert False, f"Referenced {response_type_ref=} not found"
    response_type = (
        "definitions." + response_type_ref[len("#/components/schemas/") :]
        if response_type_ref
        else "Record"
    )

    assert not "{" in key.class_name, f"{key=}"

    cls = f"""class {key.class_name}(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[{response_type}]: ...
    def get(self, {get_str}) -> Optional[{response_type}]: ...
    def filter(self, {get_str}) -> RecordSet[{response_type}]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> {response_type}: ...
    @overload
    def create(self, {create_str}) -> {response_type}: ...
    def create(self, *args: Dict[str, Any], **kwargs: Any) -> {response_type}: ...
    def update(self, objects: Iterable[{response_type}]) -> RecordSet[{response_type}]: ...
    def delete(self, objects: Iterable[{response_type}]) -> bool: ...
    def choices(self) -> dict:...
    def count(self, {get_str}) -> int: ...

"""

    return cls


def get_response_type_ref(data: dict) -> Optional[str]:
    if "get" in data:
        _200 = data["get"]["responses"]["200"]["content"]["application/json"]
        if "schema" in _200:
            schema = _200["schema"]
            if "items" in schema:
                return schema["items"]["$ref"]
            elif "$ref" in schema:
                return schema["$ref"]
            elif schema["type"] == "object":
                return None
            assert False, schema
        elif _200 == {"description": ""}:
            return None
        assert False, _200
    return None


def visit_get(data: dict) -> ParameterList:
    if "parameters" in data:
        parameters = sorted(
            data["parameters"], key=lambda x: x["name"] == "id", reverse=True
        )

        return ParameterList(
            [
                Parameter(
                    p["name"],
                    p.get("required", False),
                    PythonType.from_json(
                        p["schema"]["items"]["type"]
                        if "items" in p["schema"]
                        else p["schema"]["type"]
                    ),
                )
                for p in parameters
            ]
        )

    return ParameterList([])


def visit_create(data: dict, defs: List["RecordDefinition"]) -> ParameterList:
    try:
        parameter = data["parameters"][0]
        schema_name = parameter["schema"]["$ref"][
            len("#/components/schemas/") :
        ]
    except IndexError:
        return ParameterList([])
    except KeyError:
        schema_name = data["requestBody"]["content"]["application/json"][
            "schema"
        ]["$ref"][len("#/components/schemas/") :]
    try:
        definition: "RecordDefinition" = next(
            d for d in defs if d.name == schema_name
        )
    except StopIteration:
        assert False, f'{schema_name} not in {", ".join(d.name for d in defs)}'
    return ParameterList(
        [Parameter(p.name, p.required, p.type) for p in definition.properties]
    )


def visit_definitions(definitions: List["RecordDefinition"]) -> None:
    defs = [str(d) for d in definitions]

    header = """
from typing import Any, Dict, List, Optional, Union, Iterable
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import RecordSet, Record
from pynetbox.models import dcim
"""

    with open("pynetbox-stubs/_gen/definitions.pyi", "w") as f:
        f.write(header)
        f.write("\n".join(defs))


class Property(NamedTuple):
    name: str
    required: bool
    type: Optional[PythonType]
    ref: str = ""

    def __str__(self) -> str:
        if self.type:
            return f"{self.name}: {self.type}"
        if "#/components/schemas/" in self.ref:
            # "Nested" classes are calling "full_details" for unknown properties, so internally they
            # convert themselves to the non-nested class.
            ref = self.ref[len("#/components/schemas/") :]
            ref = ref[len("Nested") :] if ref.startswith("Nested") else ref

            if ref == "VirtualMachine":
                ref = "VirtualMachineWithConfigContext"  # TODO wild guess

            return f"{self.name}: '{ref}'"
        assert False, f"{self.name=} {self.ref=}"

    @classmethod
    def from_definition(
        cls,
        name: str,
        defi: Dict[str, Any],
        required: bool,
    ) -> "Property":
        if "$ref" in defi:
            ref = defi["$ref"]
        elif "allOf" in defi:
            ref = defi["allOf"][0]["$ref"]
        elif "items" in defi and "$ref" in defi["items"]:
            assert "$ref" in defi["items"], f"{defi=}"
            ref = defi["items"]["$ref"]
        elif "type" in defi:
            ref = ""
        else:
            assert False, f"{name=} {defi=}"
        return cls(
            name,
            required,
            PythonType.from_json(defi["type"]) if "type" in defi else None,
            ref,
        )


class RecordDefinition(NamedTuple):
    name: str
    properties: List[Property]

    def __str__(self) -> str:
        properties_str = "\n".join(
            "        self." + str(p) for p in self.properties
        )
        special_classes = {
            "Interface": "dcim.Interfaces",
            "Prefix": "ipam.Prefixes",
        }

        header = f"""class {self.name}({special_classes.get(self.name, 'Record')}):
    def __init__(self):
{properties_str}
"""
        return header

    @classmethod
    def from_dict(cls, name: str, data: Dict[str, dict]) -> "RecordDefinition":
        required: Union[dict, List] = data.get("required", [])
        properties = [
            Property.from_definition(k, d, k in required)
            for k, d in data["properties"].items()
        ]
        return cls(name, properties)

    @classmethod
    def mk_all(cls, definitions: Dict[str, dict]) -> List["RecordDefinition"]:
        return [cls.from_dict(k, d) for k, d in definitions.items()]


def main() -> None:
    with open("openapi.json", "r") as f:
        openapi = json.load(f)
    paths = openapi["paths"]
    prefixes = {p.split("/")[2] for p in paths}
    if not os.path.exists("pynetbox-stubs/_gen"):
        os.mkdir("pynetbox-stubs/_gen")

    defs = RecordDefinition.mk_all(openapi["components"]["schemas"])

    Path("pynetbox-stubs/_gen/__init__.py").touch()

    for p in prefixes:
        data = {
            path[len(f"/api/{p}/") :]: value
            for path, value in paths.items()
            if path.startswith(f"/api/{p}")
        }
        visit_prefix(p, data, defs)

    visit_definitions(defs)
    os.system("black --skip-string-normalization -l 79 pynetbox-stubs/_gen")
    os.system("isort --profile black pynetbox-stubs/_gen")


if __name__ == "__main__":
    main()
