from typing import Any


class SchemaType:
    def is_valid(self, other: Any) -> bool:
        raise NotImplementedError


class Required(SchemaType):
    pass


class Default(SchemaType):
    pass
