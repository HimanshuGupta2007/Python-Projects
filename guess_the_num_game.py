import random

randInt = random.randint(0, 101)
chances = 10

while chances > 0:
    num = int(input("Enter Number: "))

    if num == randInt:
        print("You Won!")
        break

    elif num > randInt:
        chances = chances - 1
        print("Entered number is bigger!")
        continue

    elif num < randInt:
        chances = chances - 1
        print("Entered number is smaller!")
        continue

if chances == 0:
    print("You Lost!")
