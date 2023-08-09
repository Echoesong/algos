def fizzBuzz(n):
    myRange = range(1, n + 1)
    for num in myRange:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizzBuzz(15)
