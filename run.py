import os
from sys import path
from calculator import Calculator


path.append(os.getcwd())

if __name__ == '__main__':
    mapping_dict = {'+': Calculator.add,
                    '-': Calculator.subtract,
                    '*': Calculator.multiply,
                    '/': Calculator.div}
    while True:
        print 'Please enter first number'
        a = input()
        print 'Please enter second number'
        b = input()
        print 'Please enter the operator: +,-,*,/'
        operator = raw_input()
        try:
            print mapping_dict[operator](a,b)
        except Exception:
            raise ValueError('Please enter valid operator. Supported Operators are: +, -, *, /')
