file = open('input.txt', 'r')
string = sorted(list(file.read().split()), reverse=True)
file.close()
biggest_s = ''
for i in string:
    biggest_s += i
print('The biggest number that we can make is', biggest_s)
