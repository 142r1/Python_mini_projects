import random

def roll_dice(n_sides):
    numbers = []
    roll_times = int(input("How many times do you want to roll the dice?"))
    while roll_times >= 1:
        roll = random.randint(1, n_sides)
        numbers.append(roll)
        roll_times -= 1
    print(numbers)
    print("Your total was: ")
    print(sum(numbers))
    sub_low = input("Do you want to subtract the lowest number? Enter y if yes.")
    if sub_low == 'y':
        sub_lowest(numbers)
    yn = input("Do you want to roll the same die type again? (" + str(n_sides) + ") Enter y if yes. ")
    if yn == 'y':
        roll_dice(n_sides)
    else:
        exit()

def sub_lowest(lst):
    lst.sort()
    t = len(lst)
    subbed = lst[1:t]
    print("Your total after subtracting the lowest is: ")
    print(sum(subbed))

def main():
    print("Rowan's Dice Roller sim.")
    print("")
    roll_dice(int(input("How many sides of the dice?")))

main()
