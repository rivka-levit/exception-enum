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

        self.assertEqual(
            CustomException.NotAnInteger.value,
            self.payload['code']
        )
        self.assertEqual(
            CustomException.NotAnInteger.code,
            self.payload['code']
        )
        self.assertEqual(
            CustomException.NotAnInteger.message,
            self.payload['message']
        )
        self.assertEqual(
            CustomException.NotAnInteger.exception,
            self.payload['type_name']
        )


class TestAppExceptionFunctionality(TestCase):
    """ Test exception class functionality."""

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
        """Test looking up by name."""

        self.assertEqual(
            self.exception['NotAnInteger'],
            self.exception.NotAnInteger
        )

    def test_look_up_by_code(self):
        """Test looking up by code."""

        self.assertEqual(self.exception(100), self.exception.NotAnInteger)

    def test_throw_raises_error_default_message(self):
        """Test throwing an exception when default message is used."""

        with self.assertRaises(self.payload['type_name']) as err:
            self.exception.NotAnInteger.throw()

        self.assertEqual(
            str(err.exception),
            f'{self.payload['code']} {self.payload['message']}'
        )

    def test_throw_raises_error_custom_message(self):
        """Test throwing an exception when custom message is used."""

        custom_message = 'New custom message'

        with self.assertRaises(self.payload['type_name']) as err:
            self.exception.NotAnInteger.throw(custom_message)

        self.assertEqual(
            str(err.exception),
            f'{self.payload['code']} {custom_message}'
        )
