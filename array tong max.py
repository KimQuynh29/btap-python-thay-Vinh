import random

def random_print(array, length):
    for i in range(0, length):
      array.append( random.randint(1, 10))

    print(array)

def sum(array, length, i):
    
    if(i<length):
        return array[i] + sum(array, length, i+1)
    else:
        return 0

def max_min(array, length):
    max = array[0]
    min = array[0]
    for i in range (0, length):
        if(max < array [i]):
            max = array [i]
        if(min > array[i]):
            min = array[i]
    print("\nmax = ", max)
    print("\nmin = ", min)

array=[]
length = int(input())
random_print(array, length)
print("sum = ", sum(array,length, 0))
max_min(array,length)

