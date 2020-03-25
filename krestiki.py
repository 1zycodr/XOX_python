import random

board = list(range(1, 10))

def show_board ():
    print('-------------')
    for i in range (3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')

def user_step ():
    show_board ()
    x = int(input('Куда поставить X (1 - 9): '))
    while x > 9 or x < 1:
        print('Некорректный ввод!')
        x = int(input('Куда поставить X (1 - 9): '))
    
    while str(board[x - 1]) in 'XO':
        print('Клетка уже занята!')
        x = int(input('Куда поставить X (1 - 9): '))

    board[x - 1] = 'X'

def bot_step(hard_level, game_step):
    step = 0
    if hard_level == 1:
        free = []
        for i in board:
            if str(i) not in 'XO':
                free.append(i)
        step = free[random.randint(1, len(free)) - 1]
    elif hard_level == 2:
        if game_step < 3:
            free = []
            for i in board:
                if str(i) not in 'XO':
                    free.append(i)
            step = free[random.randint(1, len(free)) - 1]
        elif game_step == 3:
            not_free = []
            for i in board:
                if str(i) in 'XO':
                    not_free.append(i)
            if board[4] in not_free and str(board[4]) == 'O':
                btype1 = [(1, 3), (1, 5), (5, 7), (3, 7)]
                btype2 = [(1, 6), (1, 8), (5, 0), (5, 6), (7, 0), (7, 2), (3, 2), (3, 8)]
                btype3 = [(1, 7), (3, 5)]
                btype4 = [(0, 2), (2, 8), (8, 6), (0, 6)]
                btype5 = [(0, 1), (1, 2), (2, 5), (5, 8), (8, 7), (7, 6), (6, 3), (3, 0)]
                btype6 = [(0, 8), (2, 6)]

                for j, i in enumerate(btype6):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0:
                            board[3] = 'O'
                            return
                        elif j == 1:
                            board[5] = 'O'
                            return
                for j, i in enumerate(btype1):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0 or j == 2:
                            board[6] = 'O'
                            return
                        elif j == 1 or j == 3:
                            board[8] = 'O'
                            return

                for j, i in enumerate(btype2):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0 or j == 4:
                            board[3] = 'O'
                            return
                        elif j == 1 or j == 5:
                            board[5] = 'O'
                            return
                        elif j == 2 or j == 6:
                            board[1] = 'O'
                            return
                        elif j == 3 or j == 7:
                            board[7] = 'O'
                            return

                for j, i in enumerate(btype3):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0:
                            board[2] = 'O'
                            return
                        elif j == 1:
                            board[8] = 'O'
                            return
                
                for j, i in enumerate(btype4):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0:
                            board[1] = 'O'
                            return
                        elif j == 1:
                            board[5] = 'O'
                            return
                        elif j == 2:
                            board[7] = 'O'
                            return
                        elif j == 3:
                            board[3] = 'O'
                            return
                
                for j, i in enumerate(btype5):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0:
                            board[2] = 'O'
                            return
                        elif j == 1:
                            board[0] = 'O'
                            return
                        elif j == 2:
                            board[8] = 'O'
                            return
                        elif j == 3:
                            board[2] = 'O'
                            return
                        elif j == 4:
                            board[6] = 'O'
                            return
                        elif j == 5:
                            board[8] = 'O'
                            return
                        elif j == 6:
                            board[0] = 'O'
                            return
                        elif j == 7:
                            board[6] = 'O'
                            return
            else:
                for j, i in enumerate([1, 2, 3, 5, 6, 7, 8]):
                    if str(board[i]) == 'X':
                        if j == 0:
                            board[7] = 'O'
                            return 
                        elif j == 1:
                            board[6] = 'O'
                            return
                        elif j == 2:
                            board[5] = 'O'
                            return
                        elif j == 3:
                            board[3] = 'O'
                            return
                        elif j == 4 or j == 6:
                            board[2] = 'O'
                            return
                        elif j == 5:
                            board[1] = 'O'
                            return
        elif game_step == 5:
            k = pre_win(board, 'O')
            if k != -1:
                board[k] = 'O'
                return
            k = pre_win(board, 'X')
            if k != -1:
                board[k] = 'O'
                return
            free = []
            for i in board:
                if str(i) not in 'XO':
                    free.append(i)
            step = free[random.randint(1, len(free)) - 1]
        elif game_step == 7:
            k = pre_win(board, 'O')
            if k != -1:
                board[k] = 'O'
                return
            
            k = pre_win(board, 'X')
            if k != -1:
                board[k] = 'O'
                return

            free = []
            for i in board:
                if str(i) not in 'XO':
                    free.append(i)
            step = free[random.randint(1, len(free)) - 1]
        else:
            k = pre_win(board, 'O')
            if k != -1:
                board[k] = 'O'
                return
            
            k = pre_win(board, 'X')
            if k != -1:
                board[k] = 'O'
                return
                
            free = []
            for i in board:
                if str(i) not in 'XO':
                    free.append(i)
            step = free[random.randint(1, len(free)) - 1]
    else:
        if game_step == 1:
            if str(board[4]) == 'X':
                step = 1
            else:
                step = 5
        elif game_step == 3:
            not_free = []
            for i in board:
                if str(i) in 'XO':
                    not_free.append(i)
            if board[4] in not_free and str(board[4]) == 'O':
                btype1 = [(1, 3), (1, 5), (5, 7), (3, 7)]
                btype2 = [(1, 6), (1, 8), (5, 0), (5, 6), (7, 0), (7, 2), (3, 2), (3, 8)]
                btype3 = [(1, 7), (3, 5)]
                btype4 = [(0, 2), (2, 8), (8, 6), (0, 6)]
                btype5 = [(0, 1), (1, 2), (2, 5), (5, 8), (8, 7), (7, 6), (6, 3), (3, 0)]
                btype6 = [(0, 8), (2, 6)]

                for j, i in enumerate(btype6):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0:
                            board[3] = 'O'
                            return
                        elif j == 1:
                            board[5] = 'O'
                            return
                for j, i in enumerate(btype1):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0 or j == 2:
                            board[6] = 'O'
                            return
                        elif j == 1 or j == 3:
                            board[8] = 'O'
                            return

                for j, i in enumerate(btype2):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0 or j == 4:
                            board[3] = 'O'
                            return
                        elif j == 1 or j == 5:
                            board[5] = 'O'
                            return
                        elif j == 2 or j == 6:
                            board[1] = 'O'
                            return
                        elif j == 3 or j == 7:
                            board[7] = 'O'
                            return

                for j, i in enumerate(btype3):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0:
                            board[2] = 'O'
                            return
                        elif j == 1:
                            board[8] = 'O'
                            return
                
                for j, i in enumerate(btype4):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0:
                            board[1] = 'O'
                            return
                        elif j == 1:
                            board[5] = 'O'
                            return
                        elif j == 2:
                            board[7] = 'O'
                            return
                        elif j == 3:
                            board[3] = 'O'
                            return
                
                for j, i in enumerate(btype5):
                    if board[i[0]] == board[i[1]] == 'X':
                        if j == 0:
                            board[2] = 'O'
                            return
                        elif j == 1:
                            board[0] = 'O'
                            return
                        elif j == 2:
                            board[8] = 'O'
                            return
                        elif j == 3:
                            board[2] = 'O'
                            return
                        elif j == 4:
                            board[6] = 'O'
                            return
                        elif j == 5:
                            board[8] = 'O'
                            return
                        elif j == 6:
                            board[0] = 'O'
                            return
                        elif j == 7:
                            board[6] = 'O'
                            return
            else:
                for j, i in enumerate([1, 2, 3, 5, 6, 7, 8]):
                    if str(board[i]) == 'X':
                        if j == 0:
                            board[7] = 'O'
                            return 
                        elif j == 1:
                            board[6] = 'O'
                            return
                        elif j == 2:
                            board[5] = 'O'
                            return
                        elif j == 3:
                            board[3] = 'O'
                            return
                        elif j == 4 or j == 6:
                            board[2] = 'O'
                            return
                        elif j == 5:
                            board[1] = 'O'
                            return
        elif game_step == 5:
            k = pre_win(board, 'O')
            if k != -1:
                board[k] = 'O'
                return
            
            k = pre_win(board, 'X')
            if k != -1:
                board[k] = 'O'
                return
            
            free = []
            for i in board:
                if str(i) not in 'XO':
                    free.append(i)
            step = free[random.randint(1, len(free)) - 1]
        elif game_step == 7:
            k = pre_win(board, 'O')
            if k != -1:
                board[k] = 'O'
                return
            
            k = pre_win(board, 'X')
            if k != -1:
                board[k] = 'O'
                return

            free = []
            for i in board:
                if str(i) not in 'XO':
                    free.append(i)
            step = free[random.randint(1, len(free)) - 1]
        else:
            k = pre_win(board, 'O')
            if k != -1:
                board[k] = 'O'
                return
            
            k = pre_win(board, 'X')
            if k != -1:
                board[k] = 'O'
                return
                
            free = []
            for i in board:
                if str(i) not in 'XO':
                    free.append(i)
            step = free[random.randint(1, len(free)) - 1]

    board[step - 1] = 'O'

def pre_win (board, val):
    pre_win_pos = [
        [0, 1, 2], [0, 3, 6], [1, 2, 0], [1, 4, 7], [2, 5, 8], [3, 4, 5],
        [3, 6, 0], [4, 7, 1], [4, 5, 3], [5, 8, 2], [6, 7, 8], [7, 8, 6],
        [0, 2, 1], [3, 5, 4], [6, 8, 7], [0, 6, 3], [1, 7, 4], [2, 8, 5],
        [0, 8, 4], [2, 6, 4], [4, 2, 6], [6, 4, 2], [0, 4, 8], [4, 8, 0]
    ]

    for i in pre_win_pos:
        if str(board[i[0]]) == str(board[i[1]]) == val and (str(board[i[2]]) not in 'XO'):
            return i[2]

    return -1

def win ():
    win_pos = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9], 
        [1, 4, 7], 
        [2, 5, 8], 
        [3, 6, 9], 
        [1, 5, 9], 
        [3, 5, 7]
    ]

    for i in win_pos:
        if str(board[i[0] - 1]) == str(board[i[1] - 1]) == str(board[i[2] - 1]) == 'X':
            return 1
        if str(board[i[0] - 1]) == str(board[i[1] - 1]) == str(board[i[2] - 1]) == 'O':
            return 2
    
    return 0

def main(board):
    step = 0

    hard_level = int(input('Введите уровень сложности (1 - 3): '))

    while hard_level not in (1, 2, 3):
        print('Некорректный ввод!')
        hard_level = int(input('Введите уровень сложности (1 - 3): '))

    while True:
        if step % 2 == 0:
            user_step()
        else:
            print("STEP:", step)
            bot_step(hard_level, step)
        
        step += 1

        if step > 4:
            if win() == 1:
                show_board()
                print('Вы победили!')
                break
            elif win() == 2:
                show_board()
                print('Вы проиграли!')
                break
        
        if step == 9:
            show_board()
            print('Ничья!')
            break

if __name__ == "__main__":
    main(board)