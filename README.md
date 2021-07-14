# **Interactive Sudoku Backtracking Visualizer**
An interactive sudoku game that visualizes the recursive backtracking algorithm. Capable of generating unique, single-solution initial board states via an extension of the same algorithm. Users can choose to solve the board themselves: left clicking an empty square on the board and subsequently entering a single-digit number will fill the space with that number if valid or remove the number if invalid; right clicking an empty square and entering a number will 'mark' the space with a superscript, a helpful feature if the user is unsure if a number may/may not be valid. At any point, the user can click on the solve button to have the board solved. Clicking on a new difficulty will refresh the board state. Built on pygame.

## **Sud.py**
Main function. Calls on GUI helper file and handles high-level actions such clearing and difficulty selection

## **Helpers**
Directory to hold back-end modules

# **sudogui.py**
Handles graphics and user interface. 

# **sudoclass.py**
Contains the sudoku class that handles generating initial board states, checking if board is valid, clearing the board, and solving. The primary backtracking function is contained here.
