# create a random bingo card

from random import randint
def createBINGO():
    d={}
    i=0

    for k in ["B","I","N","G","O"]:
        lista=[]
        for j in range(0,5):
            lista.append(randint(1,15)+15*i)
        d[k]=lista
        i=i+1
    return d
# f-ja makeBINGO radi isto što i createBINGO koristeći metod setdefault()
def makeBINGO():
    d={}
    i=0
    for k in ["B","I","N","G","O"]:
        for j in range(0,5):
            d.setdefault(k, []).append(randint(1,15)+15*i)
        i=i+1
    return d

# prethodne dve f-je rade lepo, ali prava BINGO kartica nikad ne bi imala duplikate
# tj. dva ista broja, realBINGO() se pobrine za to da duplikata nema
def realBINGO():
    d={}
    i=0

    for k in ["B","I","N","G","O"]:
        d[k]=[]
    for k in ["B","I","N","G","O"]:
        n=5
        j=0
        while j<n : 
#for j in range(0,n): ne radi jer for petlja ne dopušta da se n menja u toku rada,
# tj. možeš ga ti menjati ali on u memoriji registruje samo prvu vrednost i to je to
            temp=randint(1,15)+15*i
            duplikat=False
            if d[k]!=[]:
                for pd in d[k]:
#                    print("pd=",pd)
                    if temp==pd:
                        duplikat=True
#                        print("duplikat=",duplikat,"\t temp= ",temp)
            if duplikat == False :
                d.setdefault(k, []).append(temp)
#                print("temp->d[k] : ",temp,"\t d[k]= ",d[k], "\t k= ",k)
            else:
                n=n+1
#                print("j= ",j,"\t n= ",n)
            j=j+1
        i=i+1
    return d

def main():
    print(realBINGO())

if __name__== "__main__" : main()
