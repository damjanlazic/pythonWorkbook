# simulacija bacanja dve kockice
from random import randint


def rolaj():
    kocka1=randint(1,6)
    kocka2=randint(1,6)
    zbir=kocka1+kocka2
    return zbir
def pr(zbir):
# procenat=broj pojavljivanja zbira (zbir)/1000(broj bacanja)*100%
    prc=zbir/10
    return prc
    
def main() :
    
    z2=0
    z3=0
    z4=0
    z5=0
    z6=0
    z7=0
    z8=0
    z9=0
    z10=0
    z11=0
    z12=0
    for i in range(0,1000) :
        p=rolaj()
        if p==2 :
            z2=z2+1
        elif p==3 :
            z3=z3+1
        elif p==4 :
            z4=z4+1
        elif p==5 :
            z5=z5+1
        elif p==6 :
            z6=z6+1
        elif p==7 :
            z7=z7+1
        elif p==8 :
            z8=z8+1
        elif p==9 :
            z9=z9+1
        elif p==10 :
            z10=z10+1
        elif p==11 :
            z11=z11+1
        elif p==12 :
            z12=z12+1
        else :
            print("nešto se ovde sjebalo!")
            break
    tabela={2 : pr(z2),3:pr(z3),4:pr(z4),5:pr(z5),6:pr(z6),7:pr(z7),8:pr(z8),9:pr(z9),10:pr(z10),11:pr(z11),12:pr(z12)}
    print(tabela)

main()
