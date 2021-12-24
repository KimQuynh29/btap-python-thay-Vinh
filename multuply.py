def multiply(n):
    dem=0
    while(n>=10):
        n=n/10
        dem = dem +1
    return dem +1


n=int(input())
print('the result = ', n*pow(5, multiply(n)))