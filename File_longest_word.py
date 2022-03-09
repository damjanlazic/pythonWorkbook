# identify the longest word(s) in a file

imef=input("Unesi ime fajla: ")
fajl=open(imef,"r")
line=fajl.readline()

maxovi=[]
maxword=""

while line!="":
    i=0
    while i<len(line):
        word=""
    #    while line[i]!=" " and line[i]!="\t" and line[i]!="\n":
    #   ovo dole radi na istom principu kao ovo gore, ali je kraći zapis:
        while line[i] not in[" ",".",",",":",";","!","?", "\t", "\n","\ufeff"]:       
            word=word+line[i]
            i=i+1
# ovo je da ne bi dobio string index out of range kad dođe do kraja reda
            if i>=len(line):
                line=line+" "
        if len(maxword)<len(word):
            maxword=word
            maxovi=[]
            maxovi.append(word)
        elif len(maxword)==len(word):
            maxovi.append(word)        
        i=i+1
    line=fajl.readline()
fajl.close()

if len(maxovi)>1:
    print("najduže reči su: ",maxovi)
else: 
    print("najduža reč je: ",maxword)