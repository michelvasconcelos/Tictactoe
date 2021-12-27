import pandas as pd

print("\n", 'Instructions: Choose the position of the board you want to make a move typing the letter followed by the number on the board. Example: C3.',"\n")

while True:
    board = pd.DataFrame(columns= ['a', 'b', 'c'], index= ['1', '2', '3'])
    board = board.fillna('-')
    print(board,"\n")

    while True:

        while True:
            PlayerNoughts = input('Type position you want to put your noughts: ')
            x = PlayerNoughts[0]
            y = PlayerNoughts[1]
            if board.xs(y)[x] == '-':
                board.xs(y)[x] = '0'
                break
            else:
                print('\n', 'This is not a valid move, try another one.', '\n')

        if (board.xs('1')['a']  == '0' and board.xs('1')['b'] == '0' and board.xs('1')['c'] == '0')  or (board.xs('2')['a'] == '0' and board.xs('2')['b'] == '0' and board.xs('2')['c'] == '0') or (board.xs('3')['a'] == '0' and board.xs('3')['b'] == '0' and board.xs('3')['c'] == '0') or (board.xs('1')['a'] == '0' and board.xs('2')['a'] == '0' and board.xs('3')['a'] == '0') or (board.xs('1')['b'] == '0' and board.xs('2')['b'] == '0' and board.xs('3')['b'] == '0') or (board.xs('1')['c'] == '0' and board.xs('2')['c'] == '0' and board.xs('3')['c'] == '0') or (board.xs('1')['a'] == '0' and board.xs('2')['b'] == '0' and board.xs('3')['c'] == '0') or (board.xs('1')['c'] == '0' and board.xs('2')['b'] == '0' and board.xs('3')['a'] == '0'):
            print(board,"\n")
            print('You are the winner, Noughts player!')
            break
        elif board.xs('1')['a']  != '-' and board.xs('1')['b'] !='-' and board.xs('1')['c'] !='-'  and board.xs('2')['a'] !='-' and board.xs('2')['b'] !='-' and board.xs('2')['c'] !='-' and board.xs('3')['a'] !='-' and board.xs('3')['b'] !='-' and board.xs('3')['c'] !='-' and board.xs('1')['a'] !='-' and board.xs('2')['a'] !='-' and board.xs('3')['a'] !='-' and board.xs('1')['b'] !='-' and board.xs('2')['b'] !='-' and board.xs('3')['b'] !='-' and board.xs('1')['c'] !='-' and board.xs('2')['c'] !='-' and board.xs('3')['c'] !='-' and board.xs('1')['a'] !='-' and board.xs('2')['b'] !='-' and board.xs('3')['c'] !='-' and board.xs('1')['c'] !='-' and board.xs('2')['b'] !='-' and board.xs('3')['a'] !='-': 
            print(board,"\n")
            print('Its a tie!')
            break
        else:
            print(board,"\n")

        while True:
            PlayerCrosses = input('Type position you want to put your cross: ')
            x = PlayerCrosses[0]
            y = PlayerCrosses[1]
            if board.xs(y)[x] == '-':
                board.xs(y)[x] = 'X'
                break
            else:
                print('\n', 'This is not a valid move, try another one.', '\n')

        if (board.xs('1')['a']  == 'X' and board.xs('1')['b'] == 'X' and board.xs('1')['c'] == 'X')  or (board.xs('2')['a'] == 'X' and board.xs('2')['b'] == 'X' and board.xs('2')['c'] == 'X') or (board.xs('3')['a'] == 'X' and board.xs('3')['b'] == 'X' and board.xs('3')['c'] == 'X') or (board.xs('1')['a'] == 'X' and board.xs('2')['a'] == 'X' and board.xs('3')['a'] == 'X') or (board.xs('1')['b'] == 'X' and board.xs('2')['b'] == 'X' and board.xs('3')['b'] == 'X') or (board.xs('1')['c'] == 'X' and board.xs('2')['c'] == 'X' and board.xs('3')['c'] == 'X') or (board.xs('1')['a'] == 'X' and board.xs('2')['b'] == 'X' and board.xs('3')['c'] == 'X') or (board.xs('1')['c'] == 'X' and board.xs('2')['b'] == 'X' and board.xs('3')['a'] == 'X'):
            print(board,"\n")
            print('You are the winner, Cross player!')
            break
        else:
            print(board,"\n")

    again = input('Do you want to play again? (y/n)')
    if again == 'y':
        continue
    else:
        break


    


