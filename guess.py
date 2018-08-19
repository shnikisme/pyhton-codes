#this is guess the no. game
import random

GuessesTaken=0

print('Hello! what is your name?')
myName=input()

number=random.randint(1,200)

print('well, '+myName+', I am thinmking of a number between 1 to 200.')

for GuessesTaken in range(6):
    print('take a guess.')
    guess=input()
    guess=int(guess)

    if guess<number-10:
        print('your guess is too low.')
    elif guess>number+10:
        print('your guess is too high')
    elif guess<number:
        print('Close, but still quite low!')
    elif guess>number:
        print('Close, but still quite high!')
    else:
        break
if guess==number:
    GuessesTaken=str(GuessesTaken + 1)
    print('good job, '+myName+'! You guessed it in '+GuessesTaken+ ' guesses!')
else:
    number=str(number)
    print('Nope. I was thinkig of the number '+number+'.')
