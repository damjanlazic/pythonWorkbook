def sortipop(lista) :
    a=lista
    a.sort()
    
    print("br. elemenata je ", len(a))
    #print("br. elemenata -1 je ", brelem-1)

    g=0
    ponovo=1
    duplikat=0
    # ovaj ponovo while ne radi ne znam zašto?
    while ponovo > 0 :
        brelem=len(a)
        g=g+1
        i=0
        print("krug:",g)
        while i <= brelem-2 :
            if a[i]==a[i+1] :
                duplikat=a[i]
                print("duplikat:",duplikat)
                a.pop(i)
                brelem=len(a)
                ponovo=ponovo+1
                print("brelem=",brelem)
                print("ponovo=",ponovo)
            i=i+1
            print("kraj",i,". iteracije while i<=brelem-2\nponovo=",ponovo,"\nduplikat=",duplikat)   
        if duplikat==0 :
            ponovo=0
            print("if duplikat!=0, ponovo=",ponovo)
        


        duplikat=0
        print("kraj iteracije while ponovo>0\nponovo=",ponovo,"\nduplikat=",duplikat)
    return a

def main() :
    lista1=[5,6,7,5,7,8,9,6,5,7,4,3,2,5,5,2,1,3,2,5,6,7,8,8,6,4,3]
    a=sortipop(lista1)
    n=0
    for i in range(0,len(a)):
        print("broj ", n, ": ", a[i])
        n=n+1

main()

