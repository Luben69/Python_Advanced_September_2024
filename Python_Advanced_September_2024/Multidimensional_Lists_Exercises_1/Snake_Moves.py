rows, cols = [int(x) for x in input().split()]

sentence = input()

matrix = [['' for _ in range(cols)]for row in range(rows)]

index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = sentence[index]
            index = (index + 1) % (len(sentence))
    else:
        for col in range(cols - 1, -1, -1):
            matrix[row][col] = sentence[index]
            index = (index + 1) % (len(sentence))

for row in matrix:
    print(''.join(row))

