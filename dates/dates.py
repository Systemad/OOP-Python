import datetime
from datetime import datetime

rightNow = datetime.now()
print("Vilken datum vill du kolla hur långt det är till YYYY-MM-DD")
inputAsString = input()
datum2 = datetime.strftime(inputAsString, "%Y-%m-%d")

timediff = datum2 - rightNow
print(timediff)