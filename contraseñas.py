#Longitud: >=8
#Comb.caract: una combinación de letras (mayúsculas y minúsculas), números y símbolos especiales (como !, @, #, $, %, etc.).
#Evitar secuencias o patrones obvios: La contraseña no debe contener una secuencia simple o un patrón fácilmente reconocible como "123456" o "qwerty"
#ubic_patrones=r"C:\Users\jojohnny\Documents\git\proyectp\Proyecto_contrase-as\Proyecto_contrase-as\Patrones obvios de contraseña - Proyecto (Fundamentos de Programación SEM202415).txt"
ubic_patrones=str(input(r"ruta de ubic. patrones:"))
#ubic_contraseña=r"C:\Users\jojohnny\Documents\git\proyectp\Proyecto_contrase-as\Proyecto_contrase-as\Contraseñas - Proyecto (Fundamentos de Programación SEM202415).txt"
ubic_contraseña=str(input(r"ruta de ubic. contraseñas:"))
patrones=open(ubic_patrones)
contraseña=open(ubic_contraseña)
list_patrones=[]
list_contraseña=[]
for ciclo in patrones:
	list_patrones.append(ciclo.strip())
for ciclo in contraseña:
	list_contraseña.append(ciclo.strip())
ciclo=0
puntos=0
categoria=""
bucle=0
for bucle in range(0,len(list_contraseña),1):
	puntos+=len(list_contraseña[bucle])
	resultado="{} | {} | {}"
	for contador in range(0,len(list_contraseña[bucle]),1):
		if list_contraseña[bucle].islower()==True:
			puntos+=1
			break
	for contador in range(0,len(list_contraseña[bucle]),1):
		if list_contraseña[bucle].isupper()==True:
			puntos+=1
			break
	for contador in range(0,len(list_contraseña[bucle]),1):
		if list_contraseña[bucle].isnumeric()==True:
			puntos+=1
			break
	for contador in range(0,len(list_contraseña[bucle]),1):
		if list_contraseña[bucle].isnumeric()==False and list_contraseña[bucle].isalpha()==False:
			puntos+=1
			for contador in range(contador,len(list_contraseña[bucle]),1):
				if list_contraseña[bucle].isnumeric()==False and list_contraseña[bucle].isalpha()==False:
					puntos+=2
			break
	for contador in range(0,len(list_patrones),1):
		if list_patrones[contador] in list_contraseña[bucle]:
			puntos-=5
	if puntos<=15:
		categoria="débil"
	elif puntos>15 and puntos<=20:
		categoria="moderada"
	elif puntos>20 and puntos<=35:
		categoria="buena"
	else:
		categoria="impenetrable"
	print(resultado.format(list_contraseña[bucle],categoria,puntos))