class Nqueens:
    def __init__(self, n):
        # Initialize the board and helper variables
        self.n = n  # Size of the board (n x n)
        self.board = [-1]*self.n  # Store queen positions, index is row, value is column
        self.solutions = []  # To store all valid solutions
        self.columns = set()  # Columns where queens are already placed
        self.positive_diagonals = set()  # (row + col) diagonals
        self.negative_diagonals = set()  # (row - col) diagonals

    def solve(self):
        # Start solving from row 0
        self.backtrack(0)
        return self.solutions

    def backtrack(self, row):
        # Base case: if all rows are filled, we found a solution
        if row == self.n:
            solution = []
            for i in range(self.n):
                line = ['_ ']*self.n  # Start with all empty positions
                line[self.board[i]] = 'Q '  # Place queen at the correct column
                solution.append(''.join(line))  # Add formatted row to solution
            self.solutions.append(solution)  # Save the solution
            return  # Important to return after finding a solution

        # Try placing a queen in each column of the current row
        for col in range(self.n):
            # Skip if the column or diagonals are under attack
            if col in self.columns or row+col in self.positive_diagonals or row-col in self.negative_diagonals:
                continue

            # Place queen
            self.board[row] = col
            self.columns.add(col)
            self.positive_diagonals.add(row+col)
            self.negative_diagonals.add(row-col)

            # Recurse to next row
            self.backtrack(row+1)

            # Backtrack: remove queen and reset state
            self.columns.remove(col)
            self.positive_diagonals.remove(row+col)
            self.negative_diagonals.remove(row-col)

def main():
    # Set the number of queens explicitly (avoid using input() in restricted environments)
    N = 4  # Change this value to try different board sizes
    n_queens = Nqueens(N)
    solutions = n_queens.solve()  # Solve the problem

    # Print the results
    print(f"Total number of solutions for {N}-Queens: {len(solutions)}")
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
        print()

# Run the main function if this file is executed
if __name__ == "__main__":
    main()
