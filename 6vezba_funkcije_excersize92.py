# Odredi da li je uneti broj prost
# glavna funkcija se poziva samo ako fajl nije importovan

def jelProst(n) :
    if n == 1:
        return True
    elif n == 2 :
        return False
    else:
# u for petlji prvi parametar je uključen, a drugi nije, dakle in range(2,6)
# će dati i=2,3,4,5
        for i in range(2,n):
#kontrolni ispis za testiranje            print("i= ",i,"n%i= ", n % i)
# return izlazi iz petlje čim dobije vrednost
            if n % i == 0 :
                return False
# zbog toga ovde je dovoljno jedan broj sa kojim je n deljiv, i završili smo
# a ako ne dobije False, na kraju će dobiti True, to znači da jeste prost
    return True

def main() :
    try :
        br=int(input("Unesi neki ceo broj: "))
        if jelProst(br) == True :
            print("Broj ", br, "JESTE prost!")
        else :
            print("Broj ", br, "NIJE prost!")
#        print(jelProst(br))
    except :
        print("Koliko je teško uneti ceo broj?!")
# Zove glavnu f-ju samo ako fajl nije uvezen (imported), 
# ovo radi samo ako se glavna funkcija zove doslovno main()
if __name__ == "__main__" :
    main()

