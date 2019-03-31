from utils.decorators import validate


class Calculator(object):

    @staticmethod
    @validate
    def add(a, b):
        return a+b

    @staticmethod
    @validate
    def subtract(a,b):
        return a-b

    @staticmethod
    @validate
    def multiply(a,b):
        return a*b

    @staticmethod
    @validate
    def div(a,b):
        return a/b
