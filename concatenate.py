# izlistaj više fajlova na ekranu sve jedan za drugim
# ovo na linuxu radi komanda cat(skr. od concatenate): cat fajl1 fajl2 fajl3 itd

import sys

if len(sys.argv)<2:
    print("Napiši imena fajlova koje hoćeš da prikažemo!")
    quit()

for i in range(1,len(sys.argv)):
    try:
        fajl=open(sys.argv[i],"r")
        line=fajl.readline()
        print(sys.argv[i],"\n")
        while line!="":
            line=line.rstrip()
            print(line)
            line=fajl.readline()
        print("\n")
        fajl.close()
    except IOError:
        print("nešto ovđe smrdi...fajl ",sys.argv[i]," ili ne postoji ili si ti budala!\nA najverovatnije i jedno i drugo!\n")
    