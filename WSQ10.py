def t(s):
	x=0
	y=0
	while (x<10):
		y=y+(s[x])
		x=x+1
	return y
def a(s):
	x=f/10
	return x

def st(s):
	x=0
	y=0
	z=0
	while (x<10):
		y=((s[x])-d)**2
		x=x+1
		z=z+y
		import math 
		w=math.sqrt(z/d)
		return w
s=[]
l=0
print("List")
while (l<10):
	n=float(input("Dame un numero "))
	s.append(n)
	l=l+1
f=t(s)
d=a(s)
c=st(s)
print("total: ", f)
print("Average: ", d)
print("standar deviation ",c)