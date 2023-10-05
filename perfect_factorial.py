from decimal import Decimal, getcontext

getcontext().prec = 500

n = int(input())
factorial = Decimal(1)

if (n >= 0 and n <= 500):
    if (n == 0):
        print("Square Factorial")
    else:
        for i in range(1, n + 1):
            factorial = factorial * Decimal(i)

        square = factorial.sqrt()
        result = square == square.to_integral_value()

        if (result):
            print("Square Factorial")
        else:
            print("Not a Square Factorial")
else:
    print("Invalid input")
