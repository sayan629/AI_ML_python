s={1,2,3,3,4,5}
print(s)

s.add(7)  #adds a value
print(s)

s.remove(3)    #removes a value
print(s)

s.clear()       #empties the set
print(s)

p={1,2,3}
p.pop()         #removes a random value
print(p)

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3={7,8,9,10}
print(s1.union(s2,s3))          #returns a new union
print(s1.intersection(s2))      #return a new intersection