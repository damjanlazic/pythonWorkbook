# u terminalu kucaš python3 glava.py imefajla

import sys

if len(sys.argv)!=2:
    print("Must provide a file name as a command line parameter! ")
    quit()
    
try:
    info= open(sys.argv[1], "r")

    linija=info.readline()

    count=0
    while count<10 and linija!="":
    # bez ovog rstrip() posle svakog reda ubacuje jedan prazan red    
        linija= linija.rstrip()
        count=count+1
        print(linija)
        linija=info.readline()

    info.close()

except IOError:
    print("ERRRRORRRR, ne mere bona!")
