read_data = None
with open(r'K:\Downloads\input4.txt') as f:
    read_data = f.readlines()

drawn = list(map(int, read_data[0].strip().split(',')))

boards = []
board_stats = []
for line_num in range(2, len(read_data), 6):
    board = []
    board_status = {"rows": [5]*5, "cols": [5]*5}
    for row_line in range(line_num, line_num + 5):
        board.append(list(map(int, read_data[row_line].strip().split())))
    boards.append(board)
    board_stats.append(board_status)

board_scores = [0]*len(boards)
winner_order = []

for num in drawn:
    for board_num, board in enumerate(boards):
        if board_scores[board_num] != 0:
            continue
        for row_num, row in enumerate(board):
            for col_num, val in enumerate(row):
                if val == num:
                    board[row_num][col_num] = None
                    board_stats[board_num]["rows"][row_num] -= 1
                    board_stats[board_num]["cols"][col_num] -= 1
                    if board_stats[board_num]["rows"][row_num] == 0 or board_stats[board_num]["cols"][col_num] == 0:
                        result = val * sum([board_val for board_row in boards[board_num]
                                            for board_val in board_row if board_val is not None])
                        winner_order.append(board_num)
                        board_scores[board_num] = result

print(board_scores[winner_order[0]])
print(board_scores[winner_order[-1]])
