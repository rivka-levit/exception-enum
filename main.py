from enum import Enum, unique


@unique
class AppException(Enum):
    def __new__(cls, code, type_, message):
        member = object.__new__(cls)

        member._value_ = code
        member.code = code
        member.exception = type_
        member.message = message

        return member

    def throw(self, msg=None):
        if msg is None:
            raise self.exception(f'{self.code} {self.message}')

        raise self.exception(f'{self.code} {msg}')
