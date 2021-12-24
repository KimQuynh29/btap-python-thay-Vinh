# cau 1
import math
def compute(x):
    return 1+ 1/(1+math.exp(-x))

print("sample test 1: ", compute(0))
print("sample test 2: ", compute(1))



# cau 2


def compute_pi(n):
    result=0
    for i in range (1, n):
        result = result + (pow(-1, i+1))/(2*i-1) 
    return result

print("pi = ", 4*compute_pi(1000))
    

