def tribonacci(n):
    a = [0, 0, 1]
    for i in range(3, n):
        a.append(a[i - 3] + a[i - 2] + a[i - 1])
    return a


if __name__ == '__main__':

    n = int(input("Введите n: "))
    arr = tribonacci(n)
    print(arr)
