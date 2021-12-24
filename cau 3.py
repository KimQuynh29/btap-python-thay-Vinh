import random

def sum(array, length):
    tong=0
    for i in range (0, length):
        tong = tong + array[i]
    print("tong la ", tong)


def compute_random(array, length):

    for i in range (0, length):
        array.append(random.randint(1,10))

    print(array)
    sum(array,length)

length = int(input())
array=[]
compute_random(array, length)

