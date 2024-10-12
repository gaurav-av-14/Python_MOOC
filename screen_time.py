# Write your solution here
from datetime import datetime
dob = "290200"
date = datetime.strptime(dob,"%d%m%y")
print(date)


