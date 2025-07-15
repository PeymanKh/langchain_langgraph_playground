"""
The state schema represents the structure and types of data our graph will use.

All nodes are expected to communicate with that schema.
"""

#################### Method 1: TypeDict ####################
"""
TypeDict allows to specify keys and their data type.

This method is actually a TypeHint, It means python does NOT enforce this type while running, They are only suggested
for developers and IDE to understand the code better before runtime.
"""

from typing import TypedDict, Literal

class TypeDictState(TypedDict):
    name: str
    age: int
    gender: Literal["male", "female"]

state1 = TypeDictState(name="Peyman", age=20, gender="male")
state2 = TypeDictState(name=20.5, age="Hi", gender="cat")

# Python will run both without error...

state1['name'] = "Nomad!"  # How we edit


#################### Method 2: DataClass ####################
"""
Same as TypeDict, The difference is on definition and how we change the values.
"""

from dataclasses import dataclass

@dataclass
class DataClassState:
    name: str
    age: int
    gender: Literal["male", "female"]

state3 = DataClassState(name="Peyman", age=20, gender="male")

state3.name = "Nomad!"


#################### Method 3: Pydantic ####################
"""
Pydantic is a data validation and settings management library. It can perform validations to check whether data is same
as specified types and constraints
"""
from pydantic import BaseModel, ValidationError

class PydanticState(BaseModel):
    name: str
    age: int
    gender: Literal["male", "female"]

    # This method is for custom validation, can be skipped....
    @classmethod
    def validate_name(cls, value):
        if value not in ["male", "femail"]:
            raise ValidationError("Each gender must be either 'male' or 'femail'")

try:
    state5 = PydanticState(name="Peyman", age=20, gender="meaw")
except ValidationError as e:
    print("Validation Error:", e)

