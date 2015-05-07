def p():
	n=1
	archivo=open ('WSQ17.txt','r')
	lineas=archivo.readlines()
	for line in lineas:
		palabras=line.split(',')
		print ("El actor es: ",palabras[0])
		palabras.remove(palabras[0])
		print("Aparese en las peliculas:", ",".join(palabras))
		lineas=archivo.readlines()
		print("---------------------------------------------------------------------------------")
p()