unique_set=set()
for tuple in info: 
    unique_set.add(tuple[1])
print(unique_set)

for name,course in info:
    if(course=='English'):
        print(name)