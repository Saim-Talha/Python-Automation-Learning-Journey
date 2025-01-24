import os

directory=os.getcwd()

for roots,dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".txt"):
            print(file)
