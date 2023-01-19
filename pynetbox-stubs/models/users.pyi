from typing import List

from pynetbox.core.response import JsonField, Record

class Users(Record): ...

class Permissions(Record):
    users: List[Users]
    constraints: JsonField
