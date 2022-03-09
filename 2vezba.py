# Vežba 2 : Korišćenje if elif else i petlji while i for
# uz dodatak try & except statement-a
# Uneti niz brojeva i sortirati ih u rastućem redosledu

print("Unosite brojeve, kada završite pritisnite ENTER")

a=[]
i=1
# end=" " parametar koji se koristi da odštampa na kraju samo ono što je pod navodnicima
# umesto da pređe u novi red, što mu je default akcija
print("a[",i,"]=", end=" ")
sbroj=input()
while sbroj!="":
    if sbroj=="":
        print("Hvala!")
    else:
        try:
            broj=float(sbroj)
            a.append(broj)
            i=i+1
        except:
            print("Unesi BROJ majmune!")
    print("a[",i,"]=", end=" ")    
    sbroj=input()
   

a.sort()
for i in a:
    print("%15.8f" %i)
