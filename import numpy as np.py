import numpy as np
b=open(r"/home/honey/Documentos/uni/sem1/fund/Proyecto_contrase-as/p1.txt")
tam=0
c=open(r"/home/honey/Documentos/uni/sem1/fund/Proyecto_contrase-as/c1.txt")

def tiene_patr(palabra,patrones,valor):
    for ciclo in patrones:
        patron=ciclo.strip()
        if len(patron)<=len(palabra):
            for i in range(0,len(palabra)-1):
                if len(patron)+i<len(palabra):
                    if patron == palabra[i:len(patron)+i]:
                        valor+=5                        
    return(valor)



for a in c:
    print(tiene_patr(a,b,tam))