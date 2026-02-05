import json

# Open JSON file in read mode
with open("Data_D.json","r") as f:
    py_obj = json.load(f)   # load() reads JSON file → Python dictionary
    print(type(py_obj ))
    print(py_obj)
    
data={
    "name":"SayanPal",
    "age":27,
    "University_name":"KiiT"
}

# Open JSON file in write mode
with open("Data_D.json","w") as f:
    json.dump(data,f, indent=4)  # dump() writes Python dict → JSON file
    