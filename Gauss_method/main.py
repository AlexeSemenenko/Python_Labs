from random import randint


def generate_matrix(n):
    return [[randint(-100, 100) for i in range (0, n)] for j in range (0, n)]


def ret_x_b(matrix):
    n = len(matrix)
    vector_x = [randint(-100, 100) for i in range (0, n)]

    vector_b = []

    for i in range(0, n):
        buf = 0
        for j in range(0, n):
            buf += matrix[i][j] * vector_x[j]
        vector_b.append(buf)

    return vector_x, vector_b
'''vector_x,'''

def gauss(matrix, vector_b):
    n = len(matrix)
    for i in range(n):
        j = 0
        while j < n:
            if i != j:
                k = -1 * matrix[j][i] / matrix[i][i]
                for z in range(i, n):
                    matrix[j][z] += k * matrix[i][z]
                vector_b[j] += k * vector_b[i]
            j += 1
    for i in range(n):
        vector_b[i] /= matrix[i][i]
    return vector_b


if __name__ == '__main__':
    for i in [3, 4, 5, 6]:
        matrix = generate_matrix(i)
        x, b = ret_x_b(matrix)
        x_calculated = gauss(matrix, b)
        diff = [abs(x[i] - x_calculated[i]) for i in range(len(x))]
        print(diff)

'''matrix = []
for i in range(n):
    matrix.append(list(map(lambda x: randint(-100, 100), range(0, n))))
for i in range(n):
    for j in range(0, n):
        print(matrix[i][j], end=' ')
    print()

matrix = [[randint(-100, 100) for i in range n ] for j in range n]
'''