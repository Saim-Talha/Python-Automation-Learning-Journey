myfile=["abd.txt","abd.csv","test.txt","saim","talha.txt"]
newfile=[]

for i in myfile:
    if "a" in i:
        newfile.append(i)
print(newfile)