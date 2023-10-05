from decimal import getcontext

getcontext().prec = 20000

n = int(input())
SquareRoot = n**(1/2)
    
if(SquareRoot.is_integer()):
    parsed = int(SquareRoot)
    print(parsed)
else:
    print("Not a Perfect Square")