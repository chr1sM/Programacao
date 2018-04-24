def EscolhaDaLetra():
    # Da a escolha ao jogador sobre qual a letra ele quere.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

# the first element in the list is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def primeiroJogar():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'Jogador 2'
    else:
        return 'Jogador 1'

 #Messa
def printBoard():
    print(' | A | B | C |')
    print( '--------------')
    print( '1| '   '  | '   '  | '   '  |')
    print( '--------------')
    print( '2| '   '  | '   '  | '   '  |')
    print( '--------------')
    print( '3| '   '  | '   '  | '   '  |')
    print( '--------------')

def displayBoard():
