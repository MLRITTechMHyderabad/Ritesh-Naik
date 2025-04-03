def findTranspose(X):
    rows = len(X)
    cols = len(X[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = X[i][j]

    print(result)

X = [
    [1, 2],
    [3, 4]
]

findTranspose(X)
