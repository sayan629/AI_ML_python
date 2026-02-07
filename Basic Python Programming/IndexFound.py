nums=[10,20,47,89,45]
idx=0
x=int(input("Enter Number "))
for val in nums:
    if(val==x):
        print(f"{x} found at index={idx}")
        break
    idx+=1

 
    