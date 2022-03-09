# for u listama test proba
lista=[1,2,3,3,4,5,6,6,7,7,8,9]
n=len(lista)
i=0
print("n=",n)
while i <= n-2 :
#    print("i= ",i)
    print("lista[",i,"]= ", lista[i] )
    a=i+1
    if lista[i]== lista[a] :
        lista.pop(i)
        n=len(lista)
    i=i+1
    print("n=", n)

