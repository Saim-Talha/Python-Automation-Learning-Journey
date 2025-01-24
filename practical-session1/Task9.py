#Get the full path of current working directory
import os
print(os.path.dirname(os.path.abspath("abd.txt")))
print(os.path.abspath(os.getcwd()))