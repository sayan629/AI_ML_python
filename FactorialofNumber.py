def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

# n=int(input("Enter N:"))  for input we can use like this way
print(cal_fact(5))