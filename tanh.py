import math
def compute_tanh(x):

    return (2/(1+math.exp(-2*x))) -1
print("tanh=  ", compute_tanh(1))
    

