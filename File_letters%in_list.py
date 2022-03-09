# obrada liste reči, tako da se nađu slova koja se koriste u najmanjem broju reči
# i njihov procenat korišćenja u odnosu na ukupan broj reči

imefajla="/home/damjan/piton/words.txt"

fajl=open(imefajla,"r")


d={}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    d[ch]=0

wordcount=0
for word in fajl:
    uniquelet=[]
    wordcount=wordcount+1
    for ch in word:
        ch=ch.capitalize()
        if ch not in uniquelet and ch not in "-\'\n":
            uniquelet.append(ch)
            d[ch]=d[ch]+1
fajl.close()

minocc=min(d.values())
maxocc=max(d.values())
minlet=[]
maxlet=[]
for key in d:
    if d[key]==minocc:
        minlet.append(key)
    if d[key]==maxocc:
        maxlet.append(key)
prcmin=minocc/wordcount*100
prcmax=maxocc/wordcount*100

if len(minlet)==1:
    print("Slovo koje se pojavljuje u najmanjem broju reči je: ", minlet[0])
    print("Pojavljuje se u ",minocc," reči od ukupno ", wordcount)
    print("Procenat pojavljivanja je: %.2f" %prcmin)
else:
    print("Slova koje se pojavljuju u najmanjem broju reči su: ",minlet, end="\t")
    print("Pojavljuju se u ",minocc," reči od ukupno ", wordcount)
    print("Procenat pojavljivanja je: %.2f" %prcmin)

if len(maxlet)==1:
    print("Slovo koje se pojavljuje u najvećem broju reči je: ", maxlet[0])
    print("Pojavljuje se u ",maxocc," reči od ukupno ", wordcount)
    print("Procenat pojavljivanja je: %.2f" %prcmax)
else:
    print("Slova koje se pojavljuju u najvećembroju reči su: ",maxlet, end="\t")
    print("Pojavljuju se u ",maxocc," reči od ukupno ", wordcount)
    print("Procenat pojavljivanja je: %.2f" %prcmax)

