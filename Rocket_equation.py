import math

def rocket_equation(delta_v, exhaust_v, final_m):
    print(int(-exhaust_v + math.log10(final_m*delta_v)))

def main():
    print("Input Delta V, the rocket's exhaust velocity, and the final mass of the rocket, for the initial total mass of the rocket.")
    delta_v = int(input("Give me delta_v: "))
    exhaust_v = int(input("Give me exhaust velocity: "))
    final_m = int(input("Give me final mass of rocket: "))
    rocket_equation(delta_v, exhaust_v, final_m)

main()
