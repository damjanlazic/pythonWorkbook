#vezba koriscenja komandi print, input, operacije sa brojevima
#za dva uneta broja a i b, odrediti zbir, razliku, proizvod, kolicnik, a^b,
#...pretvori ih u integere, izvsi integersko delenje i odredi ostatak pri delenju
print("Poštovani, molimo vas da unesete dva broja...")
a = float(input("a="))
b = float(input("b="))
zbir = a + b
razlika = a - b 
proizvod = a * b
kolicnik = a / b
stepen = a ** b 
print("zbir brojeva",a, "i", b, "je", zbir)
print("razlika brojeva",a, "i", b, "je", razlika)
print("a*b=", proizvod)
print("a/b=", kolicnik)
print("broj",a, "podignut na", b, "-ti stepen je", stepen)
print(a, "podeljen sa",b, "bez ostatka je", int(a//b) )
print("Ostatak pri delenju brojeva",a, "i",b, "je",a%b)

# operacije sa integerima
a1=int(a)
b1=int(b)

k=a1//b1
ost=a1%b1
print("Količnik pri deljenju brojeva", a1, "i", b1, "bez ostatka je", k, "\na ostatak pri deljenju", ost)


