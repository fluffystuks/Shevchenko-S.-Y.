from copy import deepcopy

def filesPrint(arr):
    result = [[" - "]  + [f"|{i}|" for i in range(1, N + 1)]] + arr

    for i in range(N):
        result[i + 1].insert(0, f"|{i + 1}|")

    result = "\n".join("\t".join(map(str, line)) for line in result)
    print(result)
    return

files = [[int(num) for num in line.split()] for line in open("18.txt")]
filesCopy = deepcopy(files)
N = len(files[0])

for i in range(1, N):
    filesCopy[0][i] += filesCopy[0][i - 1]
    filesCopy[i][0] += filesCopy[i - 1][0]

verticalWalls = list((i, 5) for i in range(12, 17)) + \
                list((i, 8) for i in range(4, 20)) + \
                list((i, 13) for i in range(2, 12)) + \
                list((i, 20) for i in range(5, 11)) + \
                list((i, 18) for i in range(11, 19))

gorizontalWalls = list((5, i) for i in range(16, 20)) + \
                  list((12, i) for i in range(10, 13)) + \
                  list((17, i) for i in range(2, 5)) + \
                  list((20, i ) for i in range(5, 8)) + \
                  list((19, i) for i in range(13, 18))

endPoints = {(16, 4), (19, 7), (11, 12), (18, 17), (20, 20)}

for i in range(1, N):
    for j in range(1, N):
        coor = (i + 1, j + 1)
        
        if coor in verticalWalls:
                filesCopy[i][j] = files[i][j] + filesCopy[i - 1][j]
                
        elif coor in gorizontalWalls:
            filesCopy[i][j] = files[i][j] + filesCopy[i][j - 1]

        else:
            filesCopy[i][j] = files[i][j] + max(filesCopy[i - 1][j], filesCopy[i][j - 1])

filesPrint(files)
print()
filesPrint(filesCopy)
print()

maxSum = max([filesCopy[i - 1][j] for coor in [endPoints] for i, j in coor])
print(maxSum) #2463