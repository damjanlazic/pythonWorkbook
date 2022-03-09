# prikaži poslednjih 10 redova fajla

import sys

if len(sys.argv)!=2:
    print("Napiši ime fajla budaku nepismeni!")
    quit()

try:
#   
    fajl = open(sys.argv[1],"r")
    linija = fajl.readline()
    lista=[]


    while linija!="":

        linija=linija.rstrip()
        lista.append(linija)
        linija=fajl.readline()
    fajl.close()
#    print(lista)
    if len(lista)>10:
        for i in range(len(lista)-10,len(lista)):
            print(lista[i])
    else:
        print("mali ti ovaj fajl")
        for i in range(0,len(lista)):
            print(lista[i])

except IOError:
    print("Jes' ti bona normalan?\nUmeš li ukucat' ime fajla?")