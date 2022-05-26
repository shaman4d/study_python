print("калькулятор")
print("------------")
a=int(input("enter first number?"))
b=int(input("enter second number?"))
c=int(input("enter operation code(1:+,2:-,3:x,4:/)?"))
if c==4 and b==0:
	print("fuk u because u mistake of nature")
	y=None
elif c==1:
	y=a+b
elif c==2:
	y=a-b
elif c==3:
	y=a*b
elif c==4:
	y=a/b 
else:
	print("u dumb")
	y=None

print("резалт:"+str(y))