#from the current dire extract only .log files and read all email ids
import re
import os.path

li= os.listdir("C:\\Users\\ngupta254\\Documents\\Python\\demo")
print(li)
for i in li:
    net = os.path.splitext(i)
    if(net[1]==".log"):
        f = open("C:\\Users\\ngupta254\\Documents\\Python\\demo\\" +i,"rb")
        data = f.read().decode()
        pattern = '\S+@\S+'

        matches = re.findall(pattern, data)
        print(matches)
        f.close()