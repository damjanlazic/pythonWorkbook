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
    data={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    exprc={2:1/36,3:2/36,4:3/36,5:4/36,6:5/36,7:6/36,8:5/36,9:4/36,10:3/36,11:2/36,12:1/36}
    for i in range(1000):
        zb=rolaj()
        data[zb]=data[zb]+1
    print("zbir   procenat        očekivani (teorijski)")
    print("zbir   pojavljivanja   procenat pojavljivanja")
    for i in data:
        print("%2d %11.2f %15.2f" %(i, pr(data[i]), exprc[i]*100) )

main()
