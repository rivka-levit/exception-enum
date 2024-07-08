from unittest import TestCase

from main import AppException


class TestAppExceptionNew(TestCase):
    """Test creating an instance of AppException class."""

    def setUp(self):
        self.payload = {
            'code': 100,
            'type_name': ValueError,
            'message': 'Value is not an integer!'
        }

    def test_create_exception_class_with_instance_successfully(self):
        """Test creating an instance of exception class."""

        class CustomException(AppException):
            NotAnInteger = tuple(self.payload.values())

        self.assertEqual(CustomException.NotAnInteger.value, self.payload['code'])
        self.assertEqual(CustomException.NotAnInteger.code, self.payload['code'])
        self.assertEqual(CustomException.NotAnInteger.message, self.payload['message'])
        self.assertEqual(CustomException.NotAnInteger.type_name, self.payload['type_name'])


class TestAppExceptionFunctionality(TestCase):

    def setUp(self):
        self.name = 'NotAnInteger'
        self.payload = {
            'code': 100,
            'type_name': ValueError,
            'message': 'Value is not an integer!'
        }

        class CustomException(AppException):
            NotAnInteger = tuple(self.payload.values())

        self.exception = CustomException

    def test_look_up_by_name(self):
        self.assertEqual(self.exception['NotAnInteger'], self.exception.NotAnInteger)

    def test_look_up_by_code(self):
        self.assertEqual(self.exception(100), self.exception.NotAnInteger)
