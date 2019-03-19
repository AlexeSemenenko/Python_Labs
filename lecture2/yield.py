def tribonacci(n):
    a, b, c = 0, 0, 1
    for i in range(n):
        yield a
        a, b, c = b, c, a + b + c


if __name__ == '__main__':

    n = int(input("Введите n: "))
    for i in tribonacci(n):
        print(i)
