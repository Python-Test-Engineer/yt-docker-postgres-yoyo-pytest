from pydantic import BaseModel, ValidationError, ConfigDict, Field
import psycopg2
from rich.console import Console


console = Console()
# Python code to demonstrate namedtuple()
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple("Student", ["name", "age", "DOB"])

# Adding values
S = Student("Nandini", "19", "2541997")

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
# Employee = NamedTuple("Employee", ["id", "first_name", "last_name", "nickname"])


class Employee(BaseModel):
    model_config = ConfigDict(extras="ignore")

    employee_id: int = Field(alias="id")
    first_name: str
    last_name: str
    nickname: str | None = None


# emp = Employee(13, "John", "Cleese", "JC")
