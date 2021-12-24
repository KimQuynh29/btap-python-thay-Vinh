
def recursive( f1,  f2,  n):
    for i in range (3,n+1):
        next = f1+f2
        f1 = f2
        f2 = next
        print(next, end = ' ')
    
f1=1
f2=1
n=int(input())
print(f1, f2, end = ' ')
recursive(f1, f2, n)


