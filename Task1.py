#Given a list of tuples with info(name,subject):
  #list all unique course
  #list students enrolled in English
  #create dictionary (student,set of courses)
  
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Charlie", "English"),
    ("Alice", "Science"),    
    ("Bob", "Math"),          
    ("David", "History"),
    ("Emma", "Computer")
] 
# unique_set=set()
# for tuple in info: 
#     unique_set.add(tuple[1])
# print(unique_set)

# for name,course in info:
#     if(course=='English'):
#         print(name)

dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)
    
 
  
     

