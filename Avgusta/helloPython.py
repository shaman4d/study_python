import datetime
print("программа для вычисления року")
print("-----------------------------")
r=input("enter your birthday year?")
t=datetime.datetime.now().year
print(r)
y=t-int(r)
print("your age is "+str(y))
