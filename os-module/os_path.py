import os
for roots,dirs, files in (list(os.walk(os.getcwd()))):
    if (len(files)) != 0:
        print(roots)
        for i in files:
            print(os.path.join(roots,i))
