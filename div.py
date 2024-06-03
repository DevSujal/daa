import math
def dividewithoutdivide(dividend, divisor):
    if(dividend == 0  or dividend < divisor):
        return 0
    if(divisor == 1):
        return dividend
    return dividewithoutdivide(dividend-divisor, divisor) + 1
    


print(dividewithoutdivide(200,10))