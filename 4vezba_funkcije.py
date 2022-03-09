# funkcije
# pretvori zadatu meru u kombinaciju većih i manjih jedinica

def premeravanje(num,unit):
# try metod za slučaj da se unese nešto što će da sjebe program, 
# npr. unos slova u polje za broj (num)
    try :
# unit.lower() vraća string sa svim slovima prebačenim u mala
        unit = unit.lower()
# float(num) vraća realan broj od stringa, ako može
        num = float(num)
        if unit == "mm":
# int(a) vraća integer od decimalnog broja a tako što mu odseče decimale
            m = int(num // 1000)
            dm= int((num - m*1000) // 100)
            cm= int((num - m*1000 - dm*100) // 10)
# round(a,n) zaokružuje realan broj a na n decimalnih mesta 
            mm= round(num - m*1000 - dm*100 -cm*10, 2)
# ovaj if blok je da ako korisnik unese okrugao broj, 
# program ne bi ispisivao 0 cm 0 mm i slično (za dm nisam uradio mrzelo me)
            if cm == 0 and mm == 0: 
                rezultat = str(m) + " m i " + str(dm) +" dm"
            elif mm == 0 :
                rezultat = str(m) + " m, " + str(dm) +" dm, "+ str(cm) +" cm"
            elif cm == 0 :
                rezultat = str(m) + " m, " + str(dm) +" dm i " + str(mm) + " mm "
            else:    
                rezultat = str(m) + " m, " + str(dm) +" dm, "+ str(cm) +" cm i "+ str(mm) + " mm "
        
        elif unit == "cm":
            m = int(num // 100)
            dm= int((num - m*100) // 10)
            cm= int((num - m*100 - dm*10))
            mm= round(((num - m*100 - dm*10)*10) % 10 ,2)
            if cm == 0 and mm == 0: 
                rezultat = str(m) + " m i " + str(dm) +" dm"
            elif mm == 0 :
                rezultat = str(m) + " m, " + str(dm) +" dm, "+ str(cm) +" cm"
            elif cm == 0 :
                rezultat = str(m) + " m, " + str(dm) +" dm i " + str(mm) + " mm "
            else:    
                rezultat = str(m) + " m, " + str(dm) +" dm, "+ str(cm) +" cm i "+ str(mm) + " mm "
    
        elif unit == "dm":
            m = int(num // 10)
            dm= int((num - m*10))
            cm= int(((num - m*10)*10) % 10)
            mm= round(((((num - m*10)*10) % 10)*10) % 10, 2)
            if cm == 0 and mm == 0: 
                rezultat = str(m) + " m i " + str(dm) +" dm"
            elif mm == 0 :
                rezultat = str(m) + " m, " + str(dm) +" dm, "+ str(cm) +" cm"
            elif cm == 0 :
                rezultat = str(m) + " m, " + str(dm) +" dm i " + str(mm) + " mm "
            else:    
                rezultat = str(m) + " m, " + str(dm) +" dm, "+ str(cm) +" cm i "+ str(mm) + " mm "
        else :
            rezultat = " ...Pa dobro, jel toliko teško uneti mm, cm ili dm"
    
        
    except :
        rezultat="nemoguće uraditi! jer nisi uneo broj i jedinicu kako treba!\
                \nProbaj da uključiš mozak i pa da u polje za broj upišeš neke cifre,\
                \na u polje za jedinicu mm, cm ili dm!"
    return rezultat
broj="0"
while broj!="" :
    print("Unesi neku dužinu...(samo ENTER za kraj)")
    broj = input("broj:")
    if broj !="" :
        jed = input("jedinica:")
        print("To je ukupno ", premeravanje(broj,jed))
    else:
        print("Doviđenja, prijatno!")
