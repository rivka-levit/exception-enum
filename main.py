import enum


class AppException(enum.Enum):
    def __new__(cls, code, type_, message):
        member = object.__new__(cls)

        member._value_ = code
        member.code = code
        member.type_name = type_
        member.message = message

        return member

