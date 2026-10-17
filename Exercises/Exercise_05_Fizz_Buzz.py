
def fizzBuzz(upTo):

    for number in range(1, upTo + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=' ' )
        elif number % 3 == 0:
            print("Fizz", end=' ')
        elif number % 5 == 0:
            print("Buzz", end=' ')
        elif not number % 3 == 0 and not number % 5 == 0:
            print(number, end=' ')

fizzBuzz(35)

