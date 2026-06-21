# the above one worked very well now lets go for another round of re
import re
name = input("Name ; ")


pattern = r"\d+"
res = re.findall(pattern,name)
print(res)
if len(res) != 0:
    print("found it ")
else:
    print("all good")
