# I got help from Megan on this one
import random
from tracemalloc import start


def justright():
    print("You guessed " + str(y) + ". That is correct!")

def toolow():
    print("You guessed " + str(y) + ". That is too low!")

def toohigh():
    print("You guessed " + str(y) + ". That is too high!")

def outofrange():
    print("You guessed " + str(y) + ". That is out of the range!")

while True:

    print("Hello! Welcome to guessing game! You are about to try to guess a random generated number between your range of choice. What would you like your range to be?")
    r = input("Enter the start of your range: ")
    e = input("Enter the end of your range: ")

    print("Your range is (" + r + ", " + e + ")")
    gues = int(input("How many guesses would you like: "))

    gues1 = gues - 1

    x = random.randint(int(r),int(e))

    try:

        for count in range(0, gues):

            y = (input("You have " + str(gues) + " tires to guess the correct number between " + r + " and " + e + " or type 'q' to quit: "))
        
            if y == "q":
                quit
        
            else:
                y = int(y)

            if y == x:
                justright()
                break

            elif y > x:
                toohigh()
                if y > int(e):
                    outofrange()

            elif y < x:
                toolow()
                if y < (int(r)):
                    outofrange()


        if count == gues1:
            print("You are out of tries! " + "The correct number was " + str(x) + ". Thanks for playing!!!")
    

    except:
        print("Please enter a number")

    again = input("If you'd like to play again, please type 'yes': ")
    if again == "yes":
        start(loop)
    else:
        exit