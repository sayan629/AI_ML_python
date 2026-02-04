#basic definition of how to  calculate square of numbers from 0 to 5
squares=[]
for i in range(6):
    squares.append(i*i)

print(squares)

#------------------------------------------------------------------------------------------
#using list comprehension to calculate square of numbers from 0 to 5

thislist=[i*i for i in range(6)]
print(thislist)

# Using list comprehension with condition
# Stores square of only odd numbers

thislist1=[i*i for i in range(6) if i%2!=0]
print(thislist1)