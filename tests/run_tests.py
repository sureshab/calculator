import os
from sys import path
path.append(os.path.join(os.getcwd(), os.pardir))

import unittest
from test_calculator import CalculatorTests
from test_decorators import ValidateTests


def suite():
    suite = unittest.TestSuite()

    # Add test class here
    suite.addTest(unittest.makeSuite(CalculatorTests))
    suite.addTest(unittest.makeSuite(ValidateTests))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
