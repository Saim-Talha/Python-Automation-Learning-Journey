import os
import datetime

myfile=os.path.getctime("/home/saim/al-nafi-diploma-devops/python-automation/abd.csv")
print(myfile)

print(datetime.datetime.fromtimestamp(myfile))
