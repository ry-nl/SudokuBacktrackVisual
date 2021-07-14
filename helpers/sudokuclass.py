import random
import math
import helpers.sudogui as sg
from itertools import product

class Sudoku:

    userBoard = [[0] * 9 for i in range(9)]
    board = [[0] * 9 for i in range(9)]
    clues = [[0] * 9 for i in range(9)]


    # validrows = [[0] * 9 for i in range(9)]
    # validcols = [[0] * 9 for i in range(9)]

    numEmpty = 0
    recursions = 0

    # class constructor
    def __init__(self, difficulty):

        board = [[0] * 9 for i in range(9)]

        if difficulty == 'hard':
            self.numEmpty = 63
        if difficulty == 'medium':
            self.numEmpty = 53
        if difficulty == 'easy':
            self.numEmpty = 43

        while not self.generateBoard(0, 0):
            self.recursions = 0
            self.clearBoard()
        
        self.generatePuzzle()


    # to generate a solveable board
    def generateBoard(self, row, col):
        self.recursions += 1

        if col >= 9 and row == 8:
            return True

        if self.recursions >= 5000:
            return False

        if col > 8:
            row += 1
            col = 0

        init_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        while len(init_values) > 0:
            random_val = random.choice(init_values)
            init_values.remove(random_val)

            self.userBoard[row][col] = random_val
            self.board[row][col] = random_val

            if self.isValid(self.board, row, col):
                if self.generateBoard(row, col + 1):
                    return True
            
            self.userBoard[row][col] = 0
            self.board[row][col] = 0
        return False


    # removes elements from the generated board to "make it a puzzle"
    def generatePuzzle(self):
        for i in range(self.numEmpty):
            while True:
                row = random.randrange(0, 9)
                col = random.randrange(0, 9)

                if self.board[row][col] != 0:
                    self.userBoard[row][col] = 0
                    self.board[row][col] = 0
                    break
        
        for i in range(9):
            for j in range(9):
                self.clues[i][j] = self.board[i][j]

    # function to verify if board state is valid
    def isValid(self, board, row, col):
        value = board[row][col]

        for i in range(9):
            if i == row: continue
            if board[i][col] == value:
                return False
        
        for j in range(9):
            if j == col: continue
            if board[row][j] == value:
                return False

        box_row = math.floor(row / 3)
        box_col = math.floor(col / 3)

        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if i == row and j == col:
                    continue
                if board[i][j] == value:
                    return False

        return True


    # # function to verify if initial board is correct
    # def verify(self, board):
    #     for i in range(9):
    #         for j in range(9):
    #             if self.board[i][j] != 0:
    #                 if not self.isValid(board, i, j):
    #                     print(f'board not valid at ! {j}, {i}')
    #                     return
    #     print('valid self.board!')
    


    # recursive function to help solve board (primary backtracking function)
    def solveHelper(self, row, col):
        if col >= 9 and row == 8:
            return True

        if col > 8:
            row += 1
            col = 0

        if self.board[row][col] == 0:
            for i in range(1, 10):
                self.board[row][col] = i
                sg.decorate_square(row, col, 'insert')
                if self.isValid(self.board, row, col):
                    sg.main_loop(self, self.board, False)
                    sg.decorate_square(row, col, 'insert')
                    if self.solveHelper(row, col + 1):
                        return True

                sg.decorate_square(row, col, 'red')
                self.board[row][col] = 0
                sg.main_loop(self, self.board, False)

            return False
        
        if self.solveHelper(row, col + 1):
            return True
        return False


    # function to solve board
    def solve(self):
        if self.solveHelper(0, 0):
            return True
        return False


    # function to clear all boards
    def clearBoard(self):
        for i in range(9):
                for j in range(9):
                    self.board[i][j] = 0
                    self.userBoard[i][j] = 0
                    self.clues[i][j] = 0
    
    # # print board
    # def print(self):
    #     for row in range(9):
    #         if row % 3 == 0:
    #             print('-------------------------------')

    #         for col in range(9):
    #             if col % 3 == 0:
    #                 print('|', end = '')
    #             if self.board[row][col] != 0:
    #                 print(f' {self.board[row][col]} ', end = '')
    #             else:
    #                 print(' . ', end = '')
                
    #         print('|')
        
    #     print('-------------------------------')