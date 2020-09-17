# I got help from Megan on this one
import random


def justright():
    print("You guessed " + str(y) + ". That is correct!")

def toolow():
    print("You guessed " + str(y) + ". That is too low!")

def toohigh():
    print("You guessed " + str(y) + ". That is too high!")

def outofrange():
    print("You guessed " + str(y) + ". That is out of the range!")


x = random.randint(0,10)

try:

    for count in range(0,5):

        y = (input("Try to guess the correct number between 1 and 10 or press 'q' to quit: "))
        
        if y == q
            quit
        
        elif
            y = int(y)

        if y == x:
            justright()
            break

        elif y > x:
            toohigh()
            if y > 10:
                outofrange()

        elif y < x:
            toolow()
            if y < 0:
                outofrange()


    if count == 4:
        print("You are out of tries!")

except:
    print("Please enter a number")
