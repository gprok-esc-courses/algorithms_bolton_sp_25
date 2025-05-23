import random

size = 10
density = 30
matrix = []
next = [[0]*size for r in range(size)]

def get_alive_neighbors(row, col, matrix, size):
    n = 0
    for r in range(row-1, row+2):
        if r < 0 or r >= size:
            continue
        for c in range(col-1, col+2):
            if c < 0 or c >= size:
                continue
            n += matrix[r][c]
    n -= matrix[row][col]
    return n

for row in range(size):
    r = []
    for col in range(size):
        prob = random.randint(0, 100)
        if prob < density:
            r.append(1)
        else:
            r.append(0)
    matrix.append(r)

get_next = 'y'
gen = 1

while get_next == 'y':
    print("GEN:", gen)
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 1:
                print('X', end=' ')
            else: 
                print('-', end=' ')
        print()

    print("=================================")
    # for row in range(size):
    #     for col in range(size):
    #         print(get_alive_neighbors(row, col, matrix, size), end=' ')
    #     print()
    for row in range(size):
        for col in range(size):
            n = get_alive_neighbors(row, col, matrix, size)
            if matrix[row][col] == 1:
                if n < 2 or n > 3:
                    next[row][col] = 0
                else:
                    next[row][col] = 1
            else:
                if n == 3:
                    next[row][col] = 1
                else:
                    next[row][col] = 0
    for row in range(size):
        for col in range(size):
            matrix[row][col] = next[row][col]

    get_next = input("Continue? y/n ")
    gen += 1