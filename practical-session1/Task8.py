#Get the file name from the file path
import os
file_name=os.path.basename('root/abd.csv')
print(os.path.splitext(file_name)[0])