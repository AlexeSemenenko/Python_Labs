from enum import Enum

class Param(Enum):
    ARGS = 1
    RES = 2
    ALL = 3

def decorator(fun, Param):
    def wrapper(*args):
        res = fun(*args)
        if Param == Param.ARGS:
            print("List of args: ", *args)
        elif Param == Param.RES:
            print("Result: ", res)
        else:
            print("List of args: ", *args)
            print("Result: ", res)
        return res
    return wrapper

def sum(*args):
    res = 0
    for i in args:
        res += i
    return res


if __name__ == '__main__':

    sum = decorator(sum, Param.ARGS)
    a = sum(1, 3, 6, 8)
