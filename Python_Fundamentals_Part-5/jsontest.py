import json

json_str='{"name":"Sayan", "isTeacher":true}' 

# Check type of json_str (it is a string)
print(type(json_str))

# Convert JSON string into Python dictionary
py_obj=json.loads(json_str)

# Print type and converted Python object
print(type(py_obj),py_obj)

#python dictionary
py_object={
    "name":"Sayan",
    "isTeacher":True
}

# Check type of Python object
print(type(py_object))

# Convert Python dictionary into JSON string
json_string=json.dumps(py_object)

print(type(json_string),json_string)