# Using list comprehension to replace negative values with 0
# If value is less than 0 → replace with 0
# Else → keep the original value

lists=[-2,-3,3,4,-1,-7,2]


lists=[0 if val<0 else val for val in lists]
print(lists)