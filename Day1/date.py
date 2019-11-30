t={0:"Thursday",1:"Friday",2:"Saturday",3:"Sunday",4:"Monday",5:"Tuesday",6:"Wednesday"}
date=input("enter the date")
d=int(date)%7
print("the day is: ",t[d])
