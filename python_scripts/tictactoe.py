theBoard = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
            'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
            'LOW-L': ' ', 'LOW-M': ' ', 'LOW-R': ' '}
            
def printBoard(board):
    print(board['TOP-L'] + '|' + board['TOP-M'] + '|' + board['TOP-R'])
    print('-+-+-')
    print(board['MID-L'] + '|' + board['MID-M'] + '|' + board['MID-R'])
    print('-+-+-')
    print(board['LOW-L'] + '|' + board['LOW-M'] + '|' + board['LOW-R'])
#printBoard(theBoard)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
