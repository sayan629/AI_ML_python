n=int(input("Enter Number:"))
a=0
b=1
print(f"Fibonaci Series up to {n} terms:")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c