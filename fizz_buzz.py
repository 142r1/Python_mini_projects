def Fizz_buzz():
    for num in range(1,101):
        if num % 3 == 0:
            print("fizz")
            continue
        if num % 5 == 0:
            print('buzz')
            continue
        if num % 5 == 0 and num % 3 == 0:
            print("fizzbuzz")
            continue
        else:
            print(num)

print("fizz_buzz 1-100")
Fizz_buzz()
