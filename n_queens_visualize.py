import matplotlib.pyplot as plt
import numpy as np
from n_queens_solver import solve_n_queens

def visualize_solution(solution, n):
    """
    Visualizes a solution to the N-Queens problem.
    
    Args:
        solution: A list of column positions
        n: The size of the board
    """
    # Create a board
    board = np.zeros((n, n))
    
    # Set up the chessboard colors
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i, j] = 0.8  # Light squares
            else:
                board[i, j] = 0.3  # Dark squares
    
    plt.figure(figsize=(8, 8))
    plt.imshow(board, cmap='binary')
    
    # Place queens
    for row, col in enumerate(solution):
        plt.text(col, row, '♕', fontsize=20, ha='center', va='center')
    
    # Remove ticks
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    
    plt.title(f"{n}-Queens Solution")
    plt.show()

if __name__ == "__main__":
    n = int(input("Enter the board size (N): "))
    solutions = solve_n_queens(n)
    
    if not solutions:
        print(f"No solutions found for {n}-Queens problem.")
    else:
        print(f"Found {len(solutions)} solutions.")
        solution_idx = 0
        if len(solutions) > 1:
            max_idx = min(5, len(solutions))
            solution_idx = int(input(f"Which solution to visualize (0-{max_idx-1})? "))
        
        visualize_solution(solutions[solution_idx], n)
