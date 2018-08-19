import random

NUM_DIGITS=3
MAX_GUESS=10

def getSecretNum():
    numbers=list(range(10))
    random.shuffle(numbers)
    secretNum=''
    for i in range(NUM_DIGITS):
        secretNum+=str(numbers[i])
    return secretNum

def getClues(secretNum,guess):
    if guess==secretNum:
        return 'Congrats! your guess is correct, you have won.'

    clues=[]

    for i in range(NUM_DIGITS):
        if guess[i]==secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues)==0:
        return 'bagels'

    clues.sort()
    return ''.join(clues)

print('I am thinking of a %s-digit number. Try to guess what it is.' %(NUM_DIGITS))
print('The clues I give are...')
print('When I say:    That means:')
print(' Bagels        None of the digits is correct.')
print(' Pico          One digit is correct but in the wrong position.')
print(' Fermi         One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' %(MAX_GUESS))

    guessesTaken=1
    while guessesTaken<=MAX_GUESS:
        guess=input()

        print(getClues(secretNum,guess))
        guessesTaken+=1

        if guess==secretNum:
            break
        if guessesTaken>MAX_GUESS:
            print('you ran out of guesss. The answer was %s.'%(secretNum))

    print('Do you want to play the game again? yes or no')
    if not input().lower().startswith('y'):
        break
        
    
            
        
    
