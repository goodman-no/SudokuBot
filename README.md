Sudoku Bot
--------------------------------

This is a bot which will solve any given Sudoku puzzle.

Users can fill in any number of squares on a standard 9x9 Sudoku grid.
Then, by hitting the solve button, the program will attempt to solve the program using a backtracking algorithim.
If the puzzle is invalid in some way, the program will also determine this.

Basic Functionalities: (Progress Below)

GUI (Completed)
Users will be presented a 9 x 9 format to input any sudoku puzzle. They will be able to type in numbers 0 to 9 from their keyboard.
The GUI has been completed and the user has the option to select any square within the 9 x 9 grid to input any number by pressing a digit on the keyboard.
Determine solvability (Completed)
The puzzle will first check if the puzzle is indeed solvable by ensuring that there are no duplicate numbers in the same row, column or section. If the puzzle turns out to be unsolvable, it will report that to the user on the interface.
As the user inputs numbers on the grid when prompted, if any identical numbers are in the same row, column or 3 x 3 unit, the interface will prompt the user that the puzzle is unsolvable.
Solve puzzle if applicable (In beta)
The most practical algorithm was determined to solve given sudoku puzzles by using an ordered backtracking method. This method essentially works through every empty cell in the puzzle and tests numbers 0 to 9. When a number in a certain position is valid, it goes to the next and works through the same numbers. If the program encounters that no numbers 0 to 9 are valid in a cell, it makes it empty again and raises the value of the previous cell. Depending on the number of empty cells and the arrangement of the numbers, the amount of time necessary to solve the puzzle can vary, but from testing, puzzles of even hard rated difficulty can be solved in under 30 seconds.
