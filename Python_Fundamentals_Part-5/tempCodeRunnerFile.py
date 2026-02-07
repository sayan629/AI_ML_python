import json

json_str='{"name":"Sayan", "isTeacher":true}' 

print(type(json_str))
py_obj=json.loads(json_str)
print(type(py_obj))
