def decorator(fun):
    def wrapper(*args):
        print("List of args: ", *args)
        res = fun(*args)
        print("Result: ", res)
        return res
    return wrapper

def sum(*args):
    res = 0
    for i in args:
        res += i
    return res


if __name__ == '__main__':

    sum = decorator(sum)
    a = sum(1, 3, 6, 8)
