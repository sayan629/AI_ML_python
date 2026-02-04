f=open("D:\PYTHON_CODE\Python_Fundamentals_Part-5\Sample.txt","r") #return file object

#its read all the data in "Sample.txt"
#data=f.read()

#read the data line by line
data=f.readline()
print(data)

data=f.readline()
print(data)
f.close()       #close the txt file
