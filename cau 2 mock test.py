import math

def softmax(x, n):
    result = 0
    array=[]
    for i in range (0,n):
        result = result + math.exp(x[i])

    for j in range (0,n):
        array.append(math.exp(x[j])/result)  
    print(array)

        

x= [1.0,2.0,3.0]
n=3
softmax(x, n)

