# display tail of a file (last 10 lines) quickest and best method so far

import sys

if len(sys.argv)!=2:
    print("Daj bre ukucaj ime fajla, jes' ti pismen!?") 
    quit()

try:
    lista=[]
    fajl = open(sys.argv[1],"r")
    linija=fajl.readline()

    while linija!="":
        linija=linija.rstrip()
        lista.append(linija)
        if len(lista)>10:
            lista.pop(0)
        linija=fajl.readline()
    fajl.close()

    for i in lista:
        print(i)
except IOError:
    print("Ne mere bona, to se ne mere otvorit'!")
