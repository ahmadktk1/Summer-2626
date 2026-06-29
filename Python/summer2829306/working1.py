import os

if os.path.exists("hi.txt"):
    print("yes")
    file = open("hi.txt",'r')
else:
    print("filenotfound")
