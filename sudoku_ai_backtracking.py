import os
import time
from termcolor import colored
from copy import copy, deepcopy
import numpy as np
# A Backtracking program
# in Python to solve Sudoku problem
count = 0
# A Utility Function to print the Grid
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            if (arr[i][j] == 0):
                print (colored (arr[i][j], 'red'), end =" ")
            else:
                print (arr[i][j], end =" ")
        print ()

# Function to Find the entry in
# the Grid that is still  not used
# Searches the grid to find an
# entry that is still unassigned. If
# found, the reference parameters
# row, col will be set the location
# that is unassigned, and true is
# returned. If no unassigned entries
# remains, false is returned.
# 'l' is a list  variable that has
# been passed from the solve_sudoku function
# to keep track of incrementation
# of Rows and Columns
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

# Returns a boolean which indicates
# whether any assigned entry
# in the specified row matches
# the given number.
def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

# Returns a boolean which indicates
# whether any assigned entry
# in the specified column matches
# the given number.
def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

# Returns a boolean which indicates
# whether any assigned entry
# within the specified 3x3 box
# matches the given number
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False

# Checks whether it will be legal
# to assign num to the given row, col
# Returns a boolean which indicates
# whether it will be legal to assign
# num to the given row, col location.
def check_location_is_safe(arr, row, col, num):

    # Check if 'num' is not already
    # placed in current row,
    # current column and current 3x3 box
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,col - col % 3, num)

# Takes a partially filled-in grid
# and attempts to assign values to
# all unassigned locations in such a
# way to meet the requirements
# for Sudoku solution (non-duplication
# across rows, columns, and boxes)
def solve_sudoku(arr):
    global count
    count += 1
    # 'l' is a list variable that keeps the
    # record of row and col in
    # find_empty_location Function
    l =[0, 0]

    # If there is no unassigned
    # location, we are done
    if(not find_empty_location(arr, l)):
        return True

    # Assigning list values to row and col
    # that we got from the above Function
    row = l[0]
    col = l[1]

    # consider digits 1 to 9
    for num in range(1, 10):

        # if looks promising
        if(check_location_is_safe(arr,
                          row, col, num)):

            # make tentative assignment
            arr[row][col]= num
            os.system('cls')
            print_grid(test)
            #print()
            print(colored ("\nABOVE SUDOKU PUZZLE IS BEING SOLVED\n", 'yellow'))
            #print()
            print_grid(grid)
            print (colored ("\nNodes Expanded -->", 'yellow'), end =" ")
            print (colored (count, 'red'))
            #time.sleep(0.25)
            # return, if success,
            # ya !
            if(solve_sudoku(arr)):
                return True

            # failure, unmake & try again
            arr[row][col] = 0

    # this triggers backtracking
    return False

# Driver main function to test above functions
if __name__=="__main__":

    # creating a 2D array for the grid
    #grid =[[0 for x in range(9)]for y in range(9)]
    #test =[[0 for x in range(9)]for y in range(9)]
    # assigning values to the grid
    os.system('cls')
    fileName = input("Enter file name: ")
    if fileName.strip() == "":
        fileName = "q1.txt"
    data = open(fileName).read()
    data = [ int(eachNum) for eachNum in data.split() ]
    #print(data)
    test = np.array(data).reshape(9,9)
    print()
    print(test)
    print(colored ("\nABOVE SUDOKU PUZZLE WILL BE SOLVED using Purely Backtracking method\n", 'yellow'))
    grid = deepcopy(test)
    input("Press Enter to continue...")
    # if success print the grid
    if(solve_sudoku(grid)):
        #print_grid(grid)
        print(colored ("\nSolved...", 'yellow'))
    else:
        print ("No solution exists")
