import math

def rocket_equation(delta_v, exhaust_v, final_m):
    return(int(final_m * math.pow((2.7),(delta_v)/(exhaust_v))))

def readNumber(Prompt):
    actualNumber = None7
    while(actualNumber == None):
        number = input(Prompt)
        if number.isdigit():
            actualNumber = int(number)
        else:
            print("That's not a number.")
    return actualNumber

def main():
    print("Input Delta V, the rocket's exhaust velocity, and the final mass of the rocket, for the initial total mass of the rocket.")
    delta_v = readNumber("Give me delta_v: ")
    exhaust_v = readNumber("Give me exhaust velocity: ")
    final_m = readNumber("Give me final mass of rocket: ")
    print(rocket_equation(delta_v, exhaust_v, final_m))

main()
