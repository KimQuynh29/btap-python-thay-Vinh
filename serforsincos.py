# import math
# def mau(n):
#     if(n>0):
#         return n*mau(n-1)  
#     else:
#         return 1

# def  tu(x,  i):
#     if(i>=0):
#         return (pow(x, 2*i+1)/mau(2*i+1)) + tu(x, i-1)
#     else:
#         return 0

# print(tu(math.pi/2, 10))

import math   
def mau(n):
    result=1
    for i in range (1,n+1):
        result=result*i
    return result

def  tu( x, i):
    tong=0
    for a in range(0, i+1):
        tong = tong + (pow(x, 2*a+1)/mau(2*a+1)) 
    return tong
print(tu(math.pi/2, 10))
    
