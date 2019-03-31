def validate(func):
    def wrapper(x,y):
        valid_types = [int, float]
        if not type(x) in valid_types or not type(y) in valid_types:
            raise ValueError('Please enter numbers')
        return func(x, y)
    return wrapper
