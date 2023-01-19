from _typeshed import Incomplete
from pynetbox.core.response import JsonField, Record

class ConfigContexts(Record):
    data: JsonField

class ObjectChanges(Record):
    object_data: JsonField
    postchange_data: JsonField
    prechange_data: JsonField
