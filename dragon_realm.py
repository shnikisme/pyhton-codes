#writing the source code for the game dragon realm
import random
import time

def GameIntro():
    print('You are in a land full of dragons. In front of you,you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.Which cave will you go into? (1 or 2)')

def cave_no():
    cave=input()
    while cave!='1' and cave!='2':
        print('ERROR: wrong input. Please enter again')
        cave=input()
    return cave

def CheckCave(ChosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
    friendlyCave=random.randint(1,2)

    if ChosenCave == str(friendlyCave):
        print('Gives you his treasure! Horray! A moment of joy, you are lucky today')
    else:
        print('Gobbles you down in one bite! Alas! better luck next time.')

playAgain='yes'
while playAgain=='yes' or playAgain=='y':
    GameIntro()
    CaveNumber=cave_no()
    CheckCave(CaveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain=input()
    
