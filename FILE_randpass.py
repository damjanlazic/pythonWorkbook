# make a program that creates a random password by randomly concatenating two english words
# has to be 8 to 10 characters long, each word min 3 characters long
from random import randrange

def makepassword():
    password=""
    fajl=open("words.txt","r")
    # napravimo listu odgovarajućih reči 
    odgreči=[] 
    # pošto su reči u fajlu poređane svaka u zasebnom redu jedna linija=jedna reč
    # inače bi word bio ceo red teksta
    for word in fajl:
        if len(word)>=3 and len(word)<=7:
            # rstrip() skida \n posle svake reči            
            word=word.rstrip() 
            odgreči.append(word)
    fajl.close()
    # uzmemo jedan slučajni broj i reč sa tim rednim brojem stavimo u password
    a=randrange(0,len(odgreči))
    password=odgreči[a]

    # while ide dok se ne nađe druga reč, takva da password bude između 8 i 10 slova    
    while len(password)<8 :
        a=randrange(0,len(odgreči))
        if len(password+odgreči[a])>=8 and len(password+odgreči[a])<=10:
            password=password+odgreči[a]
    
    return password

def main():
    passw = makepassword()
    print(passw)

# main f-ja se poziva samo iz glavnog programa,
# a ne ako je funkcija importovana u drugi program
if __name__== "__main__" : 
    main()
        