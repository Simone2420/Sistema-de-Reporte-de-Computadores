from typing import TypedDict
import sqlmodel


class Computer(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    computer_number: str = sqlmodel.Field(index=True, unique=True)
    has_admin_password: bool = sqlmodel.Field(default=False)
    admin_password: str | None = sqlmodel.Field(default=None)


class ComputerFrontendDict(TypedDict):
    id: int
    computer_number: str
    has_admin_password: bool
    admin_password: str | None