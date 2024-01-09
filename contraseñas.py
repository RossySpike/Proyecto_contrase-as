from os.path import exists as verificar

ubic = ""
ubiccontr = str
ruta_contr_nueva = str
posicion = 0
puntos = 0
seguridad = str
contr = str

print("Bienvenido!")

def verif_archivo (ubicacion): #Funcion que revisa si existe un archivo

    existe = verificar(ubicacion) #usamos la funcion 'exist' de la libreria 'os.path', la funcion retorna un booleano

    if existe != True: #Si la funcion retorna True es que si existe el archivo
        print("\nError!! no se encontro el archivo, asegurate de haberlo escrito correctamente.\n")

    return (existe) #La razón de hacer esta función es porque nos pareció un buen toque comprobar si existe el archivo en cuestión, nos tomamos la libertad de usar la librería 'os' de python debido a que verificar si existe el archivo, no es un requerimiento para el proyecto

def obt_ubicacion_archivo (ubicacion,validar): 

    while True: #Ciclo infinito para asegurar que se introduzca una direccion valida

        print ("*Recuerde que tiene que incluir la extension del mismo '.txt'")
        ubicacion=str(input("Ruta --: ")) 

        if validar == True: #Hay veces que no queremos verificar si existe el archivo, como por ejemplo cuando se quiere obtener la ubicacion donde se va a crear un archivo, ya que este no existe la condicion siguiente nunca se va a cumplir y seria un bucle infinito
            if verif_archivo(ubicacion)==True:
                print("Archivo encontrado!\n")
                break

        else:
            break

    return (ubicacion)

def tiene_minusc (palabra,valor):

    for ciclo in range (0,len(palabra)):

        if palabra[ciclo].islower() == True: #.islower() es una funcion que regresa un valor booleano si TODOS los elementos de una cadena son letras minusculas
            valor += 1
            break

    return (valor)

def tiene_mayusc (palabra,valor):

    for ciclo in range (0,len(palabra)):

        if palabra[ciclo].isupper() == True:#.isupper() es una funcion que regresa un valor booleano si TODOS los elementos de una cadena son letras mayusculas
            valor += 1
            break

    return (valor)

def tiene_nmro (palabra,valor):

    for ciclo in range (0,len(palabra)):

        if palabra[ciclo].isnumeric() == True:#.isnumeric() es una funcion que regresa un valor booleano si TODOS los elementos de una cadena son numeros
            valor += 1
            break

    return (valor)

def tiene_esp_carac (palabra,valor):

    for ciclo in range (0,len(palabra)):

        if palabra[ciclo].isalnum() == False:#.isalnum() es una funcion que regresa un valor booleano si TODOS los elementos de una cadena son alfanumericos (a-z y 0-9) por lo que los unicos elementos que quedan por fuera son los caracteres especiales, que son los que queremos, es por esto que la condicion es que sea False
            valor += 3

            for ciclo in range(ciclo+1,len(palabra)):#aqui revisamos si hay mas carac. esp. en la cadena
                
                if palabra[ciclo].isalnum() == False:
                    valor += 2

            break

    return (valor)

def tiene_patr(palabra,patrones,valor):

    for ciclo in patrones:
        
        patron = ciclo.strip("\n")#Guardamos la cadena sin el salto de linea
        
        if len(patron) <= len(palabra):#Una cadena no puede contener a una cadena mas larga que ella
            
            for i in range(0,len(palabra)):
                
                if len(patron)+i <= len(palabra):#Revisamos que no se exceda el indice
                    
                    if patron == palabra[i:len(patron)+i]:
                        valor += 5
                
                else:
                    break

    return(valor)

def determinar_seguridad (categ,valor):

    if valor <= 15:
    	categ = "débil"

    elif valor > 15 and valor <= 20:
    	categ = "moderada"

    elif valor > 20 and valor <= 35:
    	categ = "buena"

    else:
    	categ = "impenetrable"   

    return (categ)

def obtener_puntos (cadena):

    for ciclo in range (len(cadena)-3,-1,-1):

        if cadena[ciclo] == "|":
            cadena=cadena[ciclo + 1 : len(cadena)]
            break

    return int(cadena)

def tam_lista (archivo):

    tam = 0

    with open (archivo,"r") as archivo:
        for ciclo in archivo:
            tam += 1

    lista=[""] * tam

    return (lista)

print("Ingrese la ruta absoluta del archivo que contiene las contraseñas.")
ubiccontr = obt_ubicacion_archivo(ubiccontr,True)
contrs_calificadas = tam_lista(ubiccontr)

print("Ingrese la ruta absoluta del archivo que contiene los patrones.")
ubicpatr = obt_ubicacion_archivo ("de patrones",ubic,True)
PATRONES = tam_lista(ubicpatr)

with open (ubicpatr,"r") as ubicpatr:
    for ciclo in ubicpatr:
        PATRONES[posicion] = ciclo
        posicion += 1

posicion = 0

with open (ubiccontr,"r") as contr_desord: 

    for ciclo in contr_desord:

        contr = ciclo.strip("\n")
        puntos = tiene_minusc (contr,puntos) + tiene_mayusc (contr,puntos) + tiene_nmro (contr,puntos) + tiene_esp_carac (contr,puntos) - tiene_patr (contr,PATRONES,puntos) + len(contr)
        seguridad = determinar_seguridad (seguridad,puntos)
        contrs_calificadas[posicion] = contr + " | " + seguridad + " | " + str(puntos)+"\n"
        puntos = 0
        posicion += 1      

for j in range (0,len(contrs_calificadas)-1):#Ordenamiento de burbuja

    for k in range(0,len(contrs_calificadas)-j-1):

        posicion = obtener_puntos(contrs_calificadas[k])

        if posicion < obtener_puntos(contrs_calificadas[k+1]):

            posicion = contrs_calificadas[k+1]
            contrs_calificadas[k+1] = contrs_calificadas[k]
            contrs_calificadas[k] = posicion

print("Ingrese la ruta absoluta donde desea guardar las contraseñas ordenadas.")
with open (obt_ubicacion_archivo(ubic,False),"w") as contr_ordenadas:    
    for ciclo in range(0,len(contrs_calificadas)):

        if ciclo != len(contrs_calificadas)-1:
            contr_ordenadas.write(contrs_calificadas[ciclo])

        else:
            contr_ordenadas.write(contrs_calificadas[ciclo].strip("\n"))

    print("Listo! el archivo con las contreñas ordenadas por nivel de seguridad ha sido exitosamente creado en la ubicación especificada.")