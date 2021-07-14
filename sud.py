from helpers.sudokuclass import Sudoku
import helpers.sudogui

puzzle = Sudoku('easy') 

while True:
    option = helpers.sudogui.main_loop(puzzle, puzzle.userBoard, True)
      
    if option > -1:
        if option == 0: puzzle.solve()
        else:
            puzzle.clearBoard()

            if option == 1: puzzle = Sudoku('easy')
            elif option == 2: puzzle = Sudoku('medium')
            elif option == 3: puzzle = Sudoku('hard')
    if option == 0:
        while helpers.sudogui.main_loop(puzzle, puzzle.board, False) == -1:
            pass
        