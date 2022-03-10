import numpy as np


              
def backtrace(first, second, matrix):
    f = [char for char in first]
    s = [char for char in second]
    new_f, new_s = [], []
    row = len(f)
    col = len(s)
    trace = [[row, col]]

    steps=[]

    while True:
        if f[row - 1] == s[col - 1]:
            cost = 0
        else:
            cost = 2

        r = matrix[row][col]
        a = matrix[row - 1][col]
        b = matrix[row - 1][col - 1]
        c = matrix[row][col - 1]

        if r == b + cost:
            # when diagonal backtrace substitution or no substitution
            if(cost != 0):
                steps.append(["Update:", row-1, col-1])
            trace.append([row - 1, col - 1])
            new_f = [f[row - 1]] + new_f
            new_s = [s[col - 1]] + new_s

            row, col = row - 1, col - 1

        else:
            # either deletion or insertion, find if minimum is up or left
            # deletion
            if r == a + 1:
                steps.append(["Delete:", row-1])
                trace.append([row - 1, col])
                #new_f = ["-"] + new_f #deleting node of first tree A (Del(Ai)) from first tree A
                # new_s = ["-"] + new_s
                new_s = [f[row - 1]] + new_s


                row, col = row - 1, col
            # insertion
            elif r == c + 1:
                steps.append(["Insert:", col-1])
                trace.append([row, col - 1])
                # new_f = ["-"] + new_f
                new_f = [s[col - 1]] + new_f #inserting node of second tree B (Ins(Bi)) in first tree A
                new_s = [s[col - 1]] + new_s

                row, col = row, col - 1

        # Exit the loop
        if row == 0 or col == 0:
            return trace, steps, new_f, new_s
 
def word_edit_distance(x, y):
    rows = len(x) + 1
    cols = len(y) + 1
    distance = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            if x[row - 1] == y[col - 1]:
                cost = 0
            else:
                cost = 2

            distance[row][col] = min(distance[row - 1][col] + 1,
                                     distance[row][col - 1] + 1,
                                     distance[row - 1][col - 1] + cost)

    print(backtrace(x, y, distance)[0])
    print(backtrace(x, y, distance)[1])
    print(backtrace(x, y, distance)[2])

    edit_distance = distance[row][col]
    return edit_distance, distance


# Driver code
if __name__ == '__main__':
     
    # roww = 7
    # coll = 7
    # word = 'AACGCA'
    # word2="GAGCTA"
    # lst = list(word)
    # lst2 = list(word2)


    # cost = [
    #         [0,1,2,3,4,5,6],
    #         [1,2,1,2,3,4,5],
    #         [2,3,2,3,4,5,4],
    #         [3,4,3,4,3,4,5],
    #         [4,3,4,3,4,5,6],
    #         [5,4,5,4,3,4,5],
    #         [6,5,4,5,4,5,4]
        
    #     ]
    # result = word_edit_distance("AACGCA", "GAGCTA")
    # print(result[0])
    # print(result[1])

    list1=[['country', 0], ['rank', 1], ['year', 2], ['gdppc', 2]]
    list2=[['country', 0], ['rank', 1], ['year', 2], ['gdppc', 2], ['rank', 1], ['year', 2], ['gdppc', 2], ['h', 2]]
    cost2 = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [1, 0, 1, 2, 3, 4, 5, 6, 7],
            [2, 1, 0, 1, 2, 3, 4, 5, 6],
            [3, 2, 1, 0, 1, 4, 3, 4, 5],
            [4, 3, 2, 1, 0, 1, 2, 3, 4]]
    print(backtrace(list1, list2, cost2)[0])
