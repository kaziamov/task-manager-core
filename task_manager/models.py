from pydantic import BaseModel


class DefaultModel(BaseModel):
    pass


class Task(DefaultModel):
    pass


class Tag(DefaultModel):
    pass


class User(DefaultModel):
    pass


class Status(DefaultModel):
    pass
