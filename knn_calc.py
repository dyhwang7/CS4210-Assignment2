import math
def euclidean_distance(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

points = [(0, 5, 0), (1, 4, 0), (2, 4, 1), (4, 4, 1), (0, 3, 0), (3, 3, 1), (4, 3, 1), (3, 2, 1), (2, 1, 0), (4, 1, 0)]

sign = {1: '+', 0: '-'}


distance_matrix = []
for i in points:
    curr_matrix = []
    for j in points:
        curr_matrix.append(euclidean_distance((i[0], i[1]), (j[0], j[1])))
    distance_matrix.append(curr_matrix)

for i in distance_matrix:
    for j in i:
        print(round(j, 3), end = '\t')
    print()

for index, row in enumerate(distance_matrix):
    lowest = 1000
    lowest_index = 0
    for j, column in enumerate(row):
        if column != 0.0 and column < lowest:
            lowest = column
            lowest_index = j

    print('for point {}, closest point is {}'.format(index, lowest_index))