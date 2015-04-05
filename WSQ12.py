def mcd(a,b):
	if (a==b):
		return a
	elif(a>b):
		y=mcd(a-b,b)
		return y
	elif(a<b):
		y=mcd(a,b-a)
		return y

a=int(input("Dame el primer valor: "))
b=int(input("Dame el segundo valor: "))
x=mcd(a,b)
print ("el maximo comun divisor de estos numero es: ",x)