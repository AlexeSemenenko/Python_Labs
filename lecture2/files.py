def tribonacci(n):
    a, b, c = 0, 0, 1
    for i in range(n):
        yield a
        a, b, c = b, c, a + b + c


if __name__ == '__main__':

    name1 = input("Введите имя файла, из которого нужно считать: ")
    f1 = open(name1, "r")

    num = int(f1.read())

    f1.close()

    name2 = input("Введите имя файла, в который нужно записать: ")
    f2 = open(name2, "w")

    count = 1
    for i in tribonacci(num):
        f2.write(str(count) + " : " + str(i) + '\n')
        count += 1

    f2.close()
