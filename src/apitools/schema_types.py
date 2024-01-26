from typing import Any, TypeVar, NoReturn

T = TypeVar("T")


class NullError(Exception):
    pass


class Null:
    def __eq__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __format__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __ge__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __getattribute__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __gt__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __hash__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __init_subclass__(self, *args: Any, **kwargs: Any) -> None:
        raise NullError("Null can't be subclassed")

    def __le__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __lt__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __ne__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __reduce__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __reduce_ex__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __repr__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __setattr__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __sizeof__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __str__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")

    def __dir__(self, *args: Any, **kwargs: Any) -> Any:
        raise NullError("Null can't be used in code")


class SchemaType:
    pass


class Required(SchemaType):
    __slots__ = ["type", "value"]

    def __init__(self, val_type: Any, *args: Any, **kwargs: Any) -> None:
        self.type = val_type
        self.value: Null = Null()


class Default(SchemaType):
    __slots__ = ["type", "value"]

    def __init__(self, val_type: T, default: T, *args: Any, **kwargs: Any) -> None:
        self.type = val_type
        self.value = default
