myfile=["abd.txt","abd.csv","test.txt","ali.txt"]
newfiles=[i.upper() for i in myfile if i != "ali.txt"]
print(newfiles)