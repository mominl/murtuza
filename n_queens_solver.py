def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns all solutions.
    
    Args:
        n: The size of the board and number of queens
    
    Returns:
        A list of solutions, each solution is a list of column positions for each row
    """
    def is_safe(board, row, col):
        # Check if a queen can be placed at board[row][col]
        
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve_util(board, col):
        # Base case: If all queens are placed
        if col >= n:
            # Add the solution
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append(j)
            solutions.append(solution)
            return True
        
        # Try placing queen in all rows of this column
        res = False
        for i in range(n):
            if is_safe(board, i, col):
                # Place the queen
                board[i][col] = 1
                
                # Recur to place rest of the queens
                res = solve_util(board, col + 1) or res
                
                # Backtrack
                board[i][col] = 0
        
        return res
    
    # Create an empty n x n board
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    # Solve the problem
    solve_util(board, 0)
    
    return solutions

def print_board(solution, n):
    """
    Prints a visual representation of a solution.
    
    Args:
        solution: A list of column positions
        n: The size of the board
    """
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'
    
    for row in board:
        print(' '.join(row))
    print()

if __name__ == "__main__":
    n = int(input("Enter the board size (N): "))
    solutions = solve_n_queens(n)
    
    print(f"Found {len(solutions)} solutions for {n}-Queens problem.")
    
    # Print first few solutions
    for i, solution in enumerate(solutions[:3]):
        print(f"Solution {i+1}:")
        print_board(solution, n)
        
    if len(solutions) > 3:
        print(f"... and {len(solutions) - 3} more solutions.")
