import random
HANGMAN_PICS=['''                 +---+
                     |
                     |
                     |
                    ===''','''
                 +---+
                 O   |
                     |
                     |
                    ===''','''
                 +---+
                 O   |
                 |   |
                     |
                    ===''','''
                 +---+
                 O   |
                /|   |
                     |
                    ===''','''
                 +---+
                 O   |
                /|\  |
                     |
                    ===''','''
                 +---+
                 O   |
                /|\  |
                /    |
                    ===''','''
                 +---+
                 O   |
                /|\  |
                / \  |
                    ===''']

words = 'ant bat bear camel cat cobra crow deer dog donkey duck eagle fox frog goat goose hawk lion lizard mole monkey moose mouse mule owl panda parrot pigeon python rabbit ram rat rhino seal shark sheep skunk snake spider swan tiger toad turkey turtle whale wolf zebra'.split()

def getRandomWord(wordList):
    index=random.randint(0,len(wordList)-1)
    return wordList[index]
def display(missedLetters,correctLetters,secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:',end=' ')
    for letter in missedLetters:
        print(letter,end=' ')
    print()

    blanks='_'*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]
    for letter in blanks:
        print(letter,end=' ')
    print()
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter:')
        guess=input()
        guess=guess.lower()
        if len(guess)!=1:
            print('enter a single letter.')
        elif guess in alreadyGuessed:
            print('letter already guessed. try another letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('enter a letter')
        else:
            return guess

def playAgain():
    print('Do you want to play again?(yes or no)')
    result=input()
    result=result.lower()
    if result=='yes':
        return True
    else:
        return False

print('H A N G M A N')
missedLetters=''
correctLetters=''
gameIsDone=False
secretWord=getRandomWord(words)

while True:
    display(missedLetters,correctLetters,secretWord)
    guess=getGuess(missedLetters+correctLetters)

    if guess in secretWord:
        correctLetters=correctLetters+guess
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False

        if foundAllLetters:
            print('congratulations! you have won. The secret word is '+secretWord)
            gameIsDone=True
    else:
        missedLetters=missedLetters+guess

        if len(missedLetters)==len(HANGMAN_PICS)-1:
            display(missedLetters,correctLetters,secretWord)
            print('you have run out of guesses!\nthe secret word is '+secretWord)
            gameIsDone=True
    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone=False
            secretWord=getRandomWord(words)
        else:
            break
            
    
        
    
