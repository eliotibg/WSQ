n=1
e=1
p=str(input("Quieres conocer el factorial de algun numero ? "))
if(p=='si' or p=='Si' or p=='SI' or p=='no' or p=='No' or p=='NO'):
	while(p=='si' or p=='SI' or p=='Si'):
		v=int(input("De que valor quieres saber el factorial: "))
		while(n<=v):
			e=e*n
			n=n+1
		print("El factorial de este numero es: ",e)
		p=str(input("Quieres conocer el factorial de algun numero ? "))
		if(p!='si' or p!='Si' or p!='SI' or p!='no' or p!='No' or p!='NO'):
			print("Error de opcion tines un intento mas ")
			p=str(input("Quieres conocer el factorial de algun numero ? "))

else:
	print("Error de opcion buelva a correr el programa ")
	p=str(input("Quieres conocer el factorial de algun numero ? "))
	if(p=='si' or p=='Si' or p=='SI' or p=='no' or p=='No' or p=='NO'):
		while(p=='si' or p=='SI' or p=='Si'):
			v=int(input("De que valor quieres saber el factorial: "))
			while(n<=v):
				e=e*n
				n=n+1
		print("El factorial de este numero es: ",e)
		p=str(input("Quieres conocer el factorial de algun numero ? "))
		if(p!='si' or p!='Si' or p!='SI' or p!='no' or p!='No' or p!='NO'):
			print("Error de opcion tines un intento mas ")
			p=str(input("Quieres conocer el factorial de algun numero ? "))