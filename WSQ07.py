r1=int(input("Dame un valor "))
r2=int(input("Dame otro valor "))
t=0
if(r2<r1):
	s=r1
	d=r2
	r1=d
	r2=s
while(r1!=r2):
	t=t+r1
	r1=r1+1
t=t+r2
print("La suma de el rango de numeros que elegiste es ",t)