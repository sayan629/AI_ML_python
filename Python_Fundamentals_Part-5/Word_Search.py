data = True  # Initialize data as True so the loop starts

line=1      # Line counter to track line numbers

word="Python"   # Word we are searching for

with open("WordSearch.txt","r") as f:    # Open the file in read mode
    
    while data:
        data=f.readline()       # Read one line from the file
        
        if(word in data):
            print(f"{word} Found at line {line}")
            break
        
        print(data)
        line+=1
    
    