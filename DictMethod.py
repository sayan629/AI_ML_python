info ={
    "name":"Sayan",
    "cgpa":9.22,
    "Subjects":["Python","AI","ML","Java","OS"]
    
}
print(info.keys())  # used to returns all keys

print(info.values()) #returns all values

print(info.items()) # returns (key,val) pairs

print(info.get("Subjects")) #return val access to Keys


info.update({               #adds new item to dict
    "state":"West Bengal"
})
print(info)