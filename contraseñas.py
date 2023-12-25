from os.path import exists as verificar

ubic = ""
ubiccontr = str
ruta_contr_nueva = str
posicion = 0
puntos = 0
formato = "{} | {} | {}\n"
seguridad = str
contr = str

print("Bienvenido!")

def verif_archivo (archivo):
    existe = verificar(archivo)
    if existe != True:
        print("\nError!! no se encontro el archivo, asegurate de haberlo escrito correctamente.\n")
    return (existe)#La razón de hacer esta función es porque nos pareció un buen toque comprobar si existe el archivo en cuestión, nos tomamos la libertad de usar la librería 'os' de python debido a que verificar si existe el archivo, no es un requerimiento para el proyecto

def obt_ubicacion_archivo (nombre_archivo,ubicacion,verificar):
    while True:
        print ("\nIntroduzca la ruta absoluta del archivo "+nombre_archivo+" *Recuerde que tiene que incluir la extension del mismo '.txt'")
        ubicacion=str(input(r"Ruta --:"))
        if verificar == True:
            if verif_archivo(ubicacion)==True:
                break
        else:
            break
    return (ubicacion)

def tiene_minusc (palabra,valor):
    for ciclo in range (0,len(palabra)):
        if palabra[ciclo].islower() == True:
            valor += 1
            break
    return (valor)

def tiene_mayusc (palabra,valor):
    for ciclo in range (0,len(palabra)):
        if palabra[ciclo].isupper() == True:
            valor += 1
            break
    return (valor)

def tiene_nmro (palabra,valor):
    for ciclo in range (0,len(palabra)):
        if palabra[ciclo].isnumeric() == True:
            valor += 1
            break
    return (valor)

def tiene_esp_carac (palabra,valor):
    for ciclo in range (0,len(palabra)):
        if palabra[ciclo].isnumeric() == False and palabra[ciclo].isalpha() == False:
            valor += 3
            for ciclo in range(ciclo+1,len(palabra)):
                if palabra[ciclo].isnumeric() == False and palabra[ciclo].isalpha() == False:
                    valor += 2
            break
    return (valor)

def tiene_patr(palabra,patrones,valor):
    for ciclo in patrones:
        patron=ciclo.strip()
        if len(patron)<=len(palabra):
            for i in range(0,len(palabra)-1):
                if len(patron)+i<len(palabra):
                    if patron == palabra[i:len(patron)+i]:
                        valor+=5 
                           
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

def obtener_nro (cadena):
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

ubiccontr = obt_ubicacion_archivo("de contra",ubiccontr,True)
contrs_calificadas = tam_lista(ubiccontr)
with open (ubiccontr,"r") as contr_desord:
   with open (obt_ubicacion_archivo ("de patrones",ubic,True),"r") as ubicpatr:
       for ciclo in contr_desord:
            contr=ciclo.strip()
            puntos=tiene_minusc (contr,puntos) + tiene_mayusc (contr,puntos) + tiene_nmro (contr,puntos) + tiene_esp_carac (contr,puntos) - tiene_patr (contr,ubicpatr,puntos) + len(contr)
            seguridad=determinar_seguridad (seguridad,puntos)
            contrs_calificadas[posicion] = contr + " | " + seguridad + " | " + str(puntos)+"\n"
            puntos=0
            posicion+=1      

for j in range (0,len(contrs_calificadas)-1):
    for k in range(0,len(contrs_calificadas)-j-1):
        posicion = obtener_nro(contrs_calificadas[k])
        posicion_sig = obtener_nro(contrs_calificadas[k+1])
        if posicion > posicion_sig:
            posicion = contrs_calificadas[k+1]
            contrs_calificadas[k+1] = contrs_calificadas[k]
            contrs_calificadas[k] = posicion

with open (obt_ubicacion_archivo("¿Donde desea guardar las contraseñas ordenadas?",ubic,False),"w") as contr_ordenadas:    
    for ciclo in range(0,len(contrs_calificadas)):
        if ciclo != len(contrs_calificadas)-1:
            contr_ordenadas.write(contrs_calificadas[ciclo])
        else:
            contr_ordenadas.write(contrs_calificadas[ciclo].strip("\n"))
print("Listo! el archivo con las contreñas ordenadas por nivel de seguridad ha sido exitosamente creado en la ubicación especificada.")
