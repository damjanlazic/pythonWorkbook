# vezba korišćenja metoda za obradu lista: pop(), sorted(), sort(), append()
# uneti niz celih brojeva poređati ih u rastućem redosledu i izbaciti sve duplikate
# ispisati niz i eliminisati željeni broj iz liste

def unos():
    print("Unosite cele brojeve, za kraj samo pritisnite ENTER:")
    i=1
    lbr=[]
    sbr= input("Broj 1: ")
    while sbr!="":
        br=int(sbr)
        lbr.append(br)
        i=i+1
        print("broj ",i,": ", end=" ")    
        sbr=input()
    return lbr
def stampajlistu(lista):
    i=1
    for br in lista :
        print("broj ",i,": ",br)
        i=i+1

def sortipop(lista) :
    a=lista
    a.sort()
    
    print("br. elemenata je ", len(a))
    #print("br. elemenata -1 je ", brelem-1)

    g=0
    ponovo=True
    duplikat=False
    # Ukoliko se pojavi bar jedan duplikat (dva ista broja) ova prva while petlja treba da se ponovi
    # to radimo pomoću dve promenljive duplikat i ponovo
    while ponovo == True :
        brelem=len(a)
        g=g+1
        i=0
        # promenljiva g i ovaj dole print služe samo kao kontrolni ispis, da bi imali uvid u to koliko puta se gornji while ponavlja
        print("krug:",g)
        duplikat=False
        while i <= brelem-2 :
# ako se nađe duplikat, briše se i br. elemenata liste (brelem) se koriguje, ali i prom. duplikat postaje True,\
# jer program ne može odmah da ispita da li postoji još istih duplikata, tako da ceo proces mora da se ponovi bar još jednom     
            if a[i]==a[i+1] :
                a.pop(i)
                brelem=len(a)
                duplikat=True
            
            i=i+1
        if duplikat==True :
            ponovo=True
        else:
            ponovo=False

    return a


def main():
    lista=unos()
    print("Uneli ste:")
    stampajlistu(lista)
    listasort=sortipop(lista)
    print("Vaša lista poređana u rastućem redosledu bez duplikata")
    stampajlistu(listasort)

main()
