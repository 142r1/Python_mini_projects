import random

def d4():
    numbers = []
    roll_times = int(input("How many times do you want to roll the d4?"))
    while roll_times >= 1:
        roll = random.randint(1,4)
        numbers.append(roll)
        roll_times -= 1
    print(numbers)
    print("Your total was: ")
    print(sum(numbers))
    sub_low = input("Do you want to subtract the lowest number? Enter y if yes.")
    if sub_low == 'y':
        sub_lowest(numbers)
    yn =input("Do you want to roll again? Enter y if yes. ")
    if yn == 'y':
        which_dice()
    else:
        exit()

def d6():
    numbers = []
    roll_times = int(input("How many times do you want to roll the d6?"))
    while roll_times >= 1:
        roll = random.randint(1,6)
        numbers.append(roll)
        roll_times -= 1
    print(numbers)
    print("Your total was: ")
    print(sum(numbers))
    sub_low = input("Do you want to subtract the lowest number? Enter y if yes.")
    if sub_low == 'y':
        sub_lowest(numbers)
    yn =input("Do you want to roll again? Enter y if yes. ")
    if yn == 'y':
        which_dice()
    else:
        exit()

def d8():
    numbers = []
    roll_times = int(input("How many times do you want to roll the d8?"))
    while roll_times >= 1:
        roll = random.randint(1,8)
        numbers.append(roll)
        roll_times -= 1
    print(numbers)
    print("Your total was: ")
    print(sum(numbers))
    sub_low = input("Do you want to subtract the lowest number? Enter y if yes.")
    if sub_low == 'y':
        sub_lowest(numbers)
    yn =input("Do you want to roll again? Enter y if yes. ")
    if yn == 'y':
        which_dice()
    else:
        exit()

def d10():
    numbers = []
    roll_times = int(input("How many times do you want to roll the d10?"))
    while roll_times >= 1:
        roll = random.randint(1,10)
        numbers.append(roll)
        roll_times -= 1
    print(numbers)
    print("Your total was: ")
    print(sum(numbers))
    sub_low = input("Do you want to subtract the lowest number? Enter y if yes.")
    if sub_low == 'y':
        sub_lowest(numbers)
    yn =input("Do you want to roll again? Enter y if yes. ")
    if yn == 'y':
        which_dice()
    else:
        exit()

def d12():
    numbers = []
    roll_times = int(input("How many times do you want to roll the d12?"))
    while roll_times >= 1:
        roll = random.randint(1,12)
        numbers.append(roll)
        roll_times -= 1
    print(numbers)
    print("Your total was: ")
    print(sum(numbers))
    sub_low = input("Do you want to subtract the lowest number? Enter y if yes.")
    if sub_low == 'y':
        sub_lowest(numbers)
    yn =input("Do you want to roll again? Enter y if yes. ")
    if yn == 'y':
        which_dice()
    else:
        exit()

def d20():
    numbers = []
    roll_times = int(input("How many times do you want to roll the d20?"))
    while roll_times >= 1:
        roll = random.randint(1,20)
        numbers.append(roll)
        roll_times -= 1
    print(numbers)
    print("Your total was: ")
    print(sum(numbers))
    sub_low = input("Do you want to subtract the lowest number? Enter y if yes.")
    if sub_low == 'y':
        sub_lowest(numbers)
    yn =input("Do you want to roll again? Enter y if yes. ")
    if yn == 'y':
        which_dice()
    else:
        exit()

def sub_lowest(lst):
    lst.sort()
    t = len(lst)
    subbed = lst[1:t]
    print("Your total after subtracting the lowest is: ")
    print(sum(subbed))

def which_dice():
    dice = input("Which dice do you want to roll? ")
    if dice == 'd4':
        d4()
    if dice == 'd6':
        d6()
    if dice == 'd8':
        d8()
    if dice == 'd10':
        d10()
    if dice == 'd12':
        d12()
    if dice == 'd20':
        d20()
    else:
        print("That isn't a valid input.")
        print("Please chose from: d4, d6, d8, d10, d12, or d20")
        which_dice()

def main():
    print("Rowan's Dice Roller sim v.1")
    print("")
    which_dice()

main()
