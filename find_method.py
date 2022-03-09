# koriscenje metoda find()

blabla="Bio jednom jedan čiča. A onda je čiča prestao da priča!\n I gotova priča?"
pos=blabla.find("!")
print(pos)
line=blabla[0:pos]
print(line)
line1=blabla[pos+1:len(blabla)]
print(line1)
fajl=open("gosh.txt","r")
print(fajl)
for word in fajl:
    pos=word.find("e")
    print(word[0:pos],end="")
    print("<",word[pos],">")



