word=input("Enter Word =")
count=0

for ch in word:
    if (ch=='a'or ch=='e' or ch=='i' or ch=='u' or ch=='o'):
        count+=1

print("Total Number of Vowels are = ",count)
        