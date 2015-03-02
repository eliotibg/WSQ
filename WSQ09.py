n=1
e=1
p=str(input("Quieres conocer el factorial de algun numero ? "))
while(p=='si' or p=='SI' or p=='Si'):
	v=int(input("De que valor quieres saber el exponente: "))
	while(n<=v):
		e=e*n
		n=n+1
	print("El expoente de este numero es: ",e)
	p=str(input("Quieres conocer el factorial de algun numero ? "))