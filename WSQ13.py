def rai (x,z):
	c=0

	y=z/x 
	if(x<y):
		i1=x
		i2=y
		x=i2
		y=i1

	while(x!=y):
		y=z/x
		x=(x+y)/2
		c=c+1
		if(y>x):
			y=x
		if (c>=1000):
			x=0
			y=0
			print("perdon esto fue muy dificil y no encontramos un numero exacto")
	return x

x=float(input("dame el valor de uno de los lados del rectangulo: "))
z=float(input("dame el area del rectangulo: "))
x=rai(x,z)
print("la rais mas aproximada de tu area es: ", x)
