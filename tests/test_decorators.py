import unittest
from mock import Mock
from utils.decorators import validate


class ValidateTests(unittest.TestCase):

    def setUp(self):
        self.test_func = Mock()
        self.test_func.return_value = True
        self.wrapped = validate(self.test_func)

    def test_validate_invalid_input(self):
        self.assertRaises(ValueError, self.wrapped, 'six', None)
        self.assertFalse(self.test_func.called, msg='Unexpected call to test_func()')

    def test_validate_success_int(self):
        self.assertEqual(self.wrapped(2,3), True)
        self.test_func.assert_called_once_with(2,3)

    def test_validate_success_float(self):
        self.assertEqual(self.wrapped(2.2,3.4), True)
        self.test_func.assert_called_with(2.2, 3.4)
