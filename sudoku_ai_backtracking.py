import time
from termcolor import colored
import copy
import os

class ai:
    def __init__(self,dimensions,file):
        self.dimensions = dimensions                                            #dimensions of the puzzle matrix
        self.nodes = 0                                                          #nodes visited expanded kept in count
        with open(file) as f_read:
            data = f_read.readlines()
            self.test = [list(x.strip()) for x in data]                         #reading the puzzle file
            #self.board = [list(x.strip()) for x in data]
        self.board = copy.deepcopy(self.test)                                   #keeping a copy for display purposes
        self.list_of_choices_list = self.get_list_of_choices_list()             #A list  of list that stores all possible choices for the
                                                                                #elements to be filled
    def display(self):
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if (self.board[i][j] == '0'):
                    print (colored (self.board[i][j], 'red'), end =" ")         #Displays the board after every move plus the nodes expanded count
                else:
                    print (self.board[i][j], end =" ")
            print ()
        print (colored ("\nNodes Expanded -->", 'yellow'), end =" ")
        print (colored (self.nodes, 'red'))

    def display_test(self):
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if (self.test[i][j] == '0'):                                    #Displays the puzzle board which the program will attempt to solve
                    print (colored (self.test[i][j], 'red'), end =" ")
                else:
                    print (self.test[i][j], end =" ")
            print ()

    def getLength(self,lst):
        if 'x' in lst or lst == []:                                             #Gets the length of the list of choices for an element...
            return 10                                                           #return 10 in case of a "given" element
        else:
            return len(lst)

    def get_location(self):
        Choice_Map = list(map(self.getLength,self.list_of_choices_list))        #Makes the map of length of list of choices and list of choices for an element
        minimum = min(Choice_Map)
        if minimum == 10:
            return (-1,-1)
        index = Choice_Map.index(minimum)                                       #gives the location of the element that has least number
        return(index // 9, index % 9)                                           #of choices

    def update_choices_list(self,row,col):
        Cell = [str(i) for i in range(1 ,self.dimensions + 1)]                  #upadates the list of list of choices by using 4 constraints
                                                                                #Constraint1: Must be a unique number
        for i in range(self.dimensions):
            if self.board[row][i] != '0':
                if self.board[row][i] in Cell:                                  #Constraint2: remove choices by checking for redundancies in the current row
                    Cell.remove(self.board[row][i])

        for i in range(self.dimensions):
            if self.board[i][col] != '0':
                if self.board[i][col] in Cell:                                  #Constraint3: remove choices by checking for redundancies in the curent column
                    Cell.remove(self.board[i][col])

        boxRow = row - row%3
        boxCol = col - col%3
        for i in range(3):
            for j in range(3):
                if self.board[boxRow+i][boxCol+j]!=0:                           #Constraint4: remove choices by checking for redundancies in the current box
                    if self.board[boxRow+i][boxCol+j] in Cell:
                        Cell.remove(self.board[boxRow+i][boxCol+j])
        return Cell

    def get_list_of_choices_list(self):
        list=[]
        for row in range(self.dimensions):
            for col in range(self.dimensions):                                  #returns the list of list of choices
                if self.board[row][col] != '0':
                    list.append(['x'])
                else:
                    list.append(self.update_choices_list(row,col))              #update the list of list is called here
        return list

    def is_choices_list_empty(self,row,col,choice):
        element = self.list_of_choices_list.pop(row*9 + col)
        if [] in self.list_of_choices_list:
            self.list_of_choices_list.insert(row*9+col,element)                 #Checks if the choices for a "element to be filled"
            return True                                                         #are exhausted or not
        else:
            self.list_of_choices_list.insert(row*9+col,element)
            return False

    def solver(self):
        location = self.get_location()                                          #Gets the location of the element with least number of choices
        if location[0] == -1:
            return True
        else:
            self.nodes+=1                                                       #Increments the nodes expanded variable
            # notgiven = self.getRemainingValues()
            row = location[0]
            col = location[1]
            for choice in self.list_of_choices_list[row*9+col]:                 #picking a choice from the list of choices for the selected element
                choice_str = str(choice)
                self.board[row][col] =  choice_str
                cpy = copy.deepcopy(self.list_of_choices_list)                  #keeping a copy in case the function backtracks
                self.list_of_choices_list = self.get_list_of_choices_list()
                os.system('cls')
                self.display_test()                                             #displaying the puzzle board
                print(colored ("\nABOVE SUDOKU PUZZLE IS BEING SOLVED\n", 'yellow'))
                self.display()                                                  #displaying the board with 0.25sec delay after every move
                time.sleep(0.25)
                if not self.is_choices_list_empty(row,col,choice_str):          #if the choices list is not exhausted the function recurrs
                    if self.solver():
                        return True
                self.board[row][col] = '0'                                      #in case the function backtracks
                self.list_of_choices_list = cpy                                 #restoring the choices list

            return False


#DRIVER CODE
os.system('cls')
fileName = input("Enter file name: ")
if fileName.strip() == "":                                                      #Aking user for the file name
    fileName = "p1"
s = ai(9,'{}.txt'.format(fileName))
print()
s.display_test()
print(colored ("\nABOVE SUDOKU PUZZLE WILL BE SOLVED using ", 'yellow'), end =" ")
print(colored ("Constraint Satisfaction ", 'red'), end =" ")                    #GUI DISPLAY
print(colored ("method \n", 'yellow'))
input("Press Enter to continue...")
if(s.solver()):
    print(colored ("\nSolved...", 'yellow'))
else:
    print ("No solution exists")                                                #Prints No solution exists if program fails
