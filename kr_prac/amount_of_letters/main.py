def string_value(string: str):
    value = 0
    for i in string:
        if i.isdigit():
            value += int(i)
        elif i.isalpha():
            value += ord(i.lower()) - 96
        else:
            value += 1
    return value


if __name__ == '__main__':
    file = open('input.txt', 'r')
    strings = []
    for line in file:
        if line != '\n':
            strings.append(line)
    strings = [line.rstrip() for line in strings]
    file.close()
    strings_with_value = {key: string_value(key) for key in strings}
    together = list(strings_with_value.items())
    together.sort(key=lambda i: i[1], reverse=True)
    for i in together:
        print('"' + i[0] + '" =', i[1])
        
