ubicpatr="patrones"
ubiccontr="contraseñas"
tamaño=0
puntos=0
formato="{} | {} | {}"
seguridad=""
def obt_ubicacion_archivo(ubicacion):
    print ("Introduzca la ruta del archivo de "+ubicacion+":")
    ubicacion=str(input(r"ruta:"))
    return (ubicacion)

def tiene_minusc (palabra,valor):
    for ciclo in range (0,len(palabra)):
        if palabra[ciclo].islower()==True:
            valor=+1
            break
    return(valor)

def tiene_mayusc (palabra,valor):
    for ciclo in range (0,len(palabra)):
        if palabra[ciclo].isupper()==True:
            valor=+1
            break
    return(valor)

def tiene_mmro (palabra,valor):
    for ciclo in range (0,len(palabra)):
        if palabra[ciclo].isnumeric()==True:
            valor+=1
            break
    return(valor)

def tiene_esp_carac (palabra,valor):
    for ciclo in range (0,len(palabra)):
        if palabra[ciclo].isnumeric()==False and palabra[ciclo].isalpha()==False:
            valor+=3
            for ciclo in range(ciclo+1,len(palabra)):
                if palabra[ciclo].isnumeric()==False and palabra[ciclo].isalpha()==False:
                    valor+=2
            break
    return(valor)

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
    if valor<=15:
    	categ="débil"
    elif valor>15 and valor<=20:
    	categ="moderada"
    elif valor>20 and valor<=35:
    	categ="buena"
    else:
    	categ="impenetrable"   
    return(categ)

ubicpatr=obt_ubicacion_archivo(ubicpatr)
ubiccontr=obt_ubicacion_archivo(ubiccontr)
ubicpatr=open(ubicpatr)
ubiccontr=open(ubiccontr)

for mainloop in ubiccontr:
    contr=mainloop.strip()
    puntos=tiene_minusc(contr,puntos)+tiene_mayusc(contr,puntos)+tiene_mmro(contr,puntos)+tiene_esp_carac(contr,puntos)-tiene_patr(contr,ubicpatr,puntos)+len(contr)
    seguridad=determinar_seguridad(seguridad,puntos)
    print(formato.format(contr,seguridad,puntos))
    puntos=0