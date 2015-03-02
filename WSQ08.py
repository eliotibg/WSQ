#Eliot Isaías Bueno Godínez
def s(x,y):
	r=x+y
	print(x ,"+",y,"=",r)
def r(x,y):
	r=x-y
	print(x,"-",y,"=",r)
def m(x,y):
	r=x*y
	print(x ,"*",y,"=",r)
def d(x,y):
	r=int(x/y)
	print(x ,"/",y,"=",r)
def re(x,y):
	r=x%y
	print("el restante de ",x ," y ",y,"=",r)
x=int(input("Dame un valor para X: "))
y=int(input("Dame un valor para Y: "))
s(x,y)
r(x,y)
m(x,y)
d(x,y)
re(x,y)