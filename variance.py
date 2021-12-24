import math
x=[5,3,6,7,4]
def compute_var(x):
    result=0
    for i in x:
        result= result + pow((i-5), 2)
    return result


print("varience = ", compute_var(x)/5)

