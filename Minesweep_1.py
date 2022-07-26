from array import array
from itertools import count
from sys import stdin
import random

"""
Function will take a 2D array and check if cells with value of 1. If 0, then set new array index to 0 automatically. 
If so, it will then check if there are at least 3 neighbors with a value of also 1. (8 max neighbors)  
If so, then set new array index to 1, otherwise 0.
"""

"""
TEST CASE:
ARRAY:  [[1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0]]
ANSWER: [[0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0]]
"""

# Determines the size of array based on level and will create a blank array and then fill with # of bombs at randomized spots. Also creates empty show array
def make_array(level):
    bomb_arr = []
    blank_count_array = []
    user_array = []
    filled_cells = []
    if level == "1":
        bombs = 4
        rows = 4
        columns = 4
    if level == "2":
        bombs = 7
        rows = 5
        columns = 5
    if level == "3":
        bombs = 10
        rows = 6
        columns = 6

    for i in range(rows):
        a = []
        b = []
        c = []
        for j in range(columns):
            a.append(0)
            b.append("x")
            c.append("-")
        bomb_arr.append(a)
        blank_count_array.append(b)
        user_array.append(c)

    while bombs > 0:
        i_spot = random.randint(0, rows - 1)
        j_spot = random.randint(0, columns - 1)
        if [i_spot, j_spot] not in filled_cells:
            filled_cells.append([i_spot, j_spot])
            bomb_arr[i_spot][j_spot] = 1
            bombs -= 1

    return bomb_arr, blank_count_array, user_array, rows, columns


def expose_zero_cells(count_array, user_array, i, j, Columns, Rows):
    # Top Left
    if i != 0 and j != 0:
        user_array[i - 1][j - 1] = count_array[i - 1][j - 1]

    # Top
    if i != 0:
        user_array[i - 1][j] = count_array[i - 1][j]

    # Top Right
    if i != 0 and j != (Columns - 1):
        user_array[i - 1][j + 1] = count_array[i - 1][j + 1]

    # left
    if j != 0:
        user_array[i][j - 1] = count_array[i][j - 1]

    # right
    if j != (Columns - 1):
        user_array[i][j + 1] = count_array[i][j + 1]

    # Botom Left
    if i != (Rows - 1) and j != 0:
        user_array[i + 1][j - 1] = count_array[i + 1][j - 1]

    # Bottom
    if i != (Rows - 1):
        user_array[i + 1][j] = count_array[i + 1][j]

    # Bottom Right
    if i != (Rows - 1) and j != (Columns - 1):
        user_array[i + 1][j + 1] = count_array[i + 1][j + 1]
    user_array[i][j]=count_array[i][j]
    return user_array


def check_neighbor_count(bomb_arr, count_array, Rows, Columns):
    for i in range(Rows):
        for j in range(Columns):
            count = int(0)

            if bomb_arr[i][j] == 0:
                # Top Left
                if i != 0 and j != 0:
                    if bomb_arr[i - 1][j - 1] == 1:
                        count += 1

                # Top
                if i != 0:
                    if bomb_arr[i - 1][j] == 1:
                        count += 1

                # Top Right
                if i != 0 and j != (Columns - 1):
                    if bomb_arr[i - 1][j + 1] == 1:
                        count += 1

                # left
                if j != 0:
                    if bomb_arr[i][j - 1] == 1:
                        count += 1

                # right
                if j != (Columns - 1):
                    if bomb_arr[i][j + 1] == 1:
                        count += 1

                # Botom Left
                if i != (Rows - 1) and j != 0:
                    if bomb_arr[i + 1][j - 1] == 1:
                        count += 1

                # Bottom
                if i != (Rows - 1):
                    if bomb_arr[i + 1][j] == 1:
                        count += 1

                # Bottom Right
                if i != (Rows - 1) and j != (Columns - 1):
                    if bomb_arr[i + 1][j + 1] == 1:
                        count += 1

                count_array[i][j] = count
    return count_array


def main():
    play = int(0)
    level = input("Choose Difficulty(1=4x4,2=5x5,3=6x6)")
    bomb_arr, blank_count_array, user_array, rows, columns = make_array(level)
    count_array = check_neighbor_count(bomb_arr, blank_count_array, rows, columns)
    print(
        count_array,
    )
    for r in user_array:
        for i in r:
            print(i, end=" ")
        print("\n")

    while play != 1:
        guess = input("Enter Spot (row, column,bomb(y/n)): ").split(",")
        guess_row = int(guess[0])
        guess_column = int(guess[1])
        bomb_spot = input("Is this a bomb? (y/Enter): ")
        if bomb_arr[guess_row][guess_column] == 1 and bomb_spot != "y":
            print("You Lose!")
            for r in count_array:
                for i in r:
                    print(i, end=" ")
                print("\n")
            exit()
        elif bomb_spot == "y":
            user_array[guess_row][guess_column] = "B"
        elif count_array[guess_row][guess_column] == 0:
            user_array = expose_zero_cells(
                count_array, user_array, guess_row, guess_column, columns, rows
            )
        else:
            user_array[guess_row][guess_column] = count_array[guess_row][guess_column]
        for r in user_array:
            for i in r:
                print(i, end=" ")
            print("\n")


if __name__ == "__main__":
    main()
