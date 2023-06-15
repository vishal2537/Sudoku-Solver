import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Separator

board = [[0] * 9 for _ in range(9)]
root = tk.Tk()
root.title("Sudoku Solver")

entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=3, font=("Arial", 30), justify="center")
        entry.grid(row=i, column=j, padx=1, pady=1, rowspan=1, columnspan=1)
        entry.config(fg="black")
        row_entries.append(entry)
    entries.append(row_entries)


def solve_sudoku():
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            if value.isdigit():
                board[i][j] = int(value)
            else:
                board[i][j] = 0
    if solve():
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(tk.END, str(board[i][j]))
    else:
        messagebox.showinfo("No Solution", "No solution found!")


def solve():
    empty_cell = find_empty_cell()
    if empty_cell is None:
        return True
    row, col = empty_cell
    for digit in range(1, 10):
        if is_valid(row, col, digit):
            board[row][col] = digit
            # Recursively solve the Sudoku
            if solve():
                return True
            # backtrack
            board[row][col] = 0
    return False


def find_empty_cell():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(row, col, digit):
    for i in range(9):
        if board[row][i] == digit or board[i][col] == digit:
            return False
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_start_row + i][box_start_col + j] == digit:
                return False
    return True


def clear_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(tk.END, "")
            board[i][j] = 0


solve_button = tk.Button(
    root, text="Solve", command=solve_sudoku, font=("Arial", 16), padx=10)
solve_button.grid(row=9, column=0, columnspan=4, pady=10)

clear_button = tk.Button(
    root, text="Clear", command=clear_board, font=("Arial", 16), padx=10)
clear_button.grid(row=9, column=5, columnspan=4, pady=10)

root.mainloop()
