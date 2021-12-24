import math
def compute( n):
    result=0
    for i in range(1, n+1):
        result = result + (-pow(0.5,i)/i)
    return result


print("sample test 1: ", compute(10))
print("sample test 2: ", compute(100))

