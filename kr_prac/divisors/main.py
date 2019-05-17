def get_divisors(number):
    i = 2
    divisors = []
    while i * i <= number:
        while number % i == 0:
            divisors.append(i)
            number /= i
        i += 1
    if number > 1:
        divisors.append(int(number))
    return divisors


def result_string(number, divisors):
    string = str(number) + ' = '
    buf = divisors[0]
    count = 0
    for current in divisors:
        if current == buf:
            count += 1
        else:
            if count != 1:
                string += str(buf) + '^' + str(count) + ' * '
            else:
                string += str(buf) + ' * '
            buf = current
            count = 1
    if count != 1:
        string += str(buf) + '^' + str(count)
    else:
        string += str(buf)
    return string


if __name__ == '__main__':
    numbers_s = set()
    file = open('input.txt', 'r')
    for line in file:
        numbers_s.update(map(int, line.split()))
    file.close()
    for i in sorted(numbers_s):
        print(result_string(i, get_divisors(i)))
