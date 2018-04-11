import random
import os

# initialize a 2048 matrix. return a matrix list
def init():
    matrix = [ 0 for i in range(16) ]
    random_lst = random.sample(range(16), 2) # generate 2 different number
    matrix[random_lst[0]] = matrix[random_lst[1]] = 2
    return matrix


def isOver(matrix):
    if 0 in matrix:
        return False
    else:
        # inspect horizontal line
        for i in range(4, 16):
            if matrix[i] == matrix[i-4]:
                return False
        # inspect vertical line
        for i in range(0, 16):
            if i % 4 != 0:
                if matrix[i] == matrix[i-1]:
                    return False
    return True


def isWin(matrix):
    if max(matrix) >= 2048:
        print("        You Win!")
        return True


def isSame(matrix_old, matrix_new):
    if matrix_old == matrix_new:
        print("matrix is same , choose another direction!")
        return True


# print matrix
def printMatrix(matrix):
    print("+-----+-----+-----+-----+")
    for i in range(0, 4):
        for j in range(0, 4):
            if matrix[4*i+j] != 0:
                print("|" + " "*(4-len(str(matrix[4*i+j]))) + str(matrix[4*i+j]) + " ", end="")
            else:
                print("|     ", end="")
        print("|")
        print("+-----+-----+-----+-----+")


def move(matrix, direction):
    mergedList = []
    if direction == "w":
        for n in range(16):
            i = n
            while i > 3:
                if matrix[i] != 0:
                    if matrix[i-4] == matrix[i] and i not in mergedList:
                        matrix[i-4]*=2
                        matrix[i] = 0
                        mergedList.append(i)
                        mergedList.append(i - 4)
                    elif matrix[i-4] == 0:
                        matrix[i-4] = matrix[i]
                        matrix[i] = 0
                i -= 4

    elif direction == "a":
        for n in range(16):
            i = n
            while i%4 !=0:
                if matrix[i] != 0:
                    if matrix[i - 1] == matrix[i] and i not in mergedList:
                        matrix[i - 1] *= 2
                        matrix[i] = 0
                        mergedList.append(i)
                        mergedList.append(i - 1)
                    elif matrix[i - 1] == 0:
                        matrix[i - 1] = matrix[i]
                        matrix[i] = 0
                i -= 1

    elif direction == "s":
        for n in range(15, -1, -1):
            i = n
            while i < 12:
                if matrix[i] != 0:
                    if matrix[i + 4] == matrix[i] and i not in mergedList:
                        matrix[i + 4] *= 2
                        matrix[i] = 0
                        mergedList.append(i)
                        mergedList.append(i + 4)
                    elif matrix[i + 4] == 0:
                        matrix[i + 4] = matrix[i]
                        matrix[i] = 0
                i += 4

    elif direction == "d":
        for n in range(15, -1, -1):
            i = n
            while i%4 != 3:
                if matrix[i] != 0:
                    if matrix[i + 1] == matrix[i] and i not in mergedList:
                        matrix[i + 1] *= 2
                        matrix[i] = 0
                        mergedList.append(i)
                        mergedList.append(i + 1)
                    elif matrix[i + 1] == 0:
                        matrix[i + 1] = matrix[i]
                        matrix[i] = 0
                i += 1
    return matrix


def add(matrix):
    getZeroIndex = []
    for i in range(0, 16):
        if matrix[i] == 0:
            getZeroIndex.append(i)
    if getZeroIndex != []:
        matrix[random.choice(getZeroIndex)] = 2
    return matrix


def play():
    matrix = init()
    step = 0
    matrix_stack = []
    matrix_stack.append(list(matrix))
    os.system("clear")

    while isOver(matrix) != True:
        printMatrix(matrix)
        print("        step:", step)
        isWin(matrix)
        inp = input()
        if inp in ["w", "a", "s", "d"]:
            matrix = move(matrix, inp)
            if isSame(matrix, matrix_stack[-1]):
                input()
                os.system("clear")
                continue
            matrix = add(matrix)
            matrix_stack.append(list(matrix))
            step += 1
        if inp == "q":
            print("Bye Bye!")
            exit()
        os.system("clear")
    print("Game Over! You lose!")


if __name__ == '__main__':
    play()
