# number the lines in a file. Create a new file from a file requested by user


ime=input("Unesite ime fajla: ")
ime2="novi"+ime
try:
    fajl1=open(ime,"r")
    fajl2=open(ime2,"w")
    line=fajl1.readline()
    count=0

    while line!="":
        
        count=count+1
        line=str(count)+": " + line
        fajl2.write(line)
# rstrip() treba samo za ispis na ekran, zato što print() automatski dodaje svoj novi red
# moglo bi se uraditi i bez rstrip()-a, ovako: print(line,end="")
#        line=line.rstrip()
        print(line,end="")
        line=fajl1.readline()
    fajl1.close()
    fajl2.close()
    
except IOError:
    print("Da ti nisi iz prosvete pobego'?\nPa dobro jel ni ime fajla ne umeš da uneseš?")
