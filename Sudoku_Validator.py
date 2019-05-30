def sudoku(board):
    flag = 0  # declar to store for checking condition
    # step 1 : Checking if the input is right format column
    if len(board) != 9:
        return f"Invalid Format"

    else:
        # step 2 : checking if the input is right format row
        for i in range(len(board)):
            if len(board[i]) == 9:
                continue
            else:
                flag = 1
        if flag == 1:
            return f"Invalid Format"

        # step 3 : checking for the right format sudoku
        # step 1 : checking the row of sudoku (how) if you set the list and the len is < 9 it duplicate
        else:
            if row_dup(board) == 1:
                return f"Not Finished"
            else:
                # step 2 : checking the column of sudoku (how)
                # make a new 2 Dimensional list
                if col_dup(board) == 1:
                    win = getBlocks(board)
                    if win == 0:
                        return f"Finished"
                    else:
                        return f"Not Finished"
                else:
                    return f"Not Finished"


def row_dup(board):
    count = 0
    for i in range(len(board)):
        af_set = set(board[i])
        if len(af_set) < 9:
            count = count + 1
        else:
            continue
    if count == 0:
        return 0
    else:
        return 1


def col_dup(board):
    i = 0
    new_board = []
    while i < len(board):
        j = 0
        temp = []
        while j < len(board):
            temp.append(board[j][i])
            j += 1
        i += 1
        new_board.append(temp)
    count = 0
    for i in range(len(new_board)):
        af_set = set(new_board[i])
        if len(af_set) < 9:
            count = count + 1
        else:
            continue
    if count == 0:
        return 1
    else:
        return 0


def getBlocks(board):
    res = 0
    answer = []
    check = 0
    for r in range(3):
        for c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[3 * r + i][3 * c + j])
            answer.append(block)
    final_list = []
    for i in range(9):
        for j in range(9):
            res = res + answer[i][j]
        final_list.append(res)
        res = 0
    for x in final_list:
        if x != 45:
            check = 1
            break
        else:
            continue
    return check
