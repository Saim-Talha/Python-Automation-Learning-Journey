import os
print("My old path is: "+ os.getcwd())
my_path="/home/"
mydir=str(os.chdir(my_path))
print("we are changing the path from linux terminal" + mydir)
print("My new path is: " + os.getcwd())
