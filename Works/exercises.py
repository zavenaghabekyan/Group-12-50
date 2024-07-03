# def fibonacci(n):
#     if n <= 0:
#         return "Invalid input. Fibonacci sequence starts from index 1."
    
#     fib_list = [0, 1]
    
#     # Calculate Fibonacci sequence up to nth term
#     for i in range(2, n+1):
#         next_fib = fib_list[-1] + fib_list[-2]
#         fib_list.append(next_fib)
    
#     return fib_list[n]

# # Example usage:
# n = 100  # Calculate the 100th Fibonacci number
# result = fibonacci(n)
# print(f"The {n}th Fibonacci number is: {result}")
# ----------------------------------------------------------------------------------


# def print_chess_board():
#     board_size = 8
#     board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    
#     # Заполнение шахматной доски
#     for row in range(board_size):
#         for col in range(board_size):
#             if (row + col) % 2 == 1:
#                 board[row][col] = '#'
    
#     # Вывод шахматной доски на экран
#     for row in range(board_size):
#         for col in range(board_size):
#             print(board[row][col], end=' ')
#         print()

# # Вызов функции для печати шахматной доски
# print_chess_board()
