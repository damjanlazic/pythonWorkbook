# find the percentage of occuring for all letters in the alphabet
# in a list of words

filename="words.txt"

inf=open(filename,"r")
contains={}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    contains[ch]=0
wordcount=0
# number of unique words in text
unique=[]
marks=True
novareč=""
for word in inf:

    for ch in word:
        ch=ch.capitalize()
#        print(ch)
        if ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ-\'" :
            if marks==False: 
                if novareč not in unique:
                    unique.append(novareč)
                novareč=""
                marks=True
        else:
            if marks==True:
                novareč=novareč+ch
                wordcount=wordcount+1
                marks=False

#        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ-\'":
            else:
                novareč=novareč+ch
                marks=False
                if ch not in "-\'":
                    contains[ch]=contains[ch]+1
            
inf.close()
maxocc=0
totalletters=0
minocc=min(contains.values())
for ch in contains:
#    print(ch)
    if contains[ch]>maxocc:
        maxocc=contains[ch]
        maxletter=ch
    if minocc==contains[ch]:
        minletter=ch
    totalletters=totalletters+contains[ch]


print(contains)
print("Most occuring letter is:", maxletter,"occurs: ",maxocc," times")
print("Least occuring letter is:", minletter,"occurs: ",minocc," times")


# Ovaj deo programa broji samo koliko različitih reči u tekstu sadrži u sebi svako od slova
# ako sadrži neko slovo više puta u istoj reči, broji se samo jednom
dick={}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    dick[ch]=0
print("unique words in text are:", unique)
for word in unique:
    uniqueletters=[]
    for ch in word:
        if ch not in uniqueletters and ch not in "-\'":
            uniqueletters.append(ch)
            dick[ch]=dick[ch]+1    
minletval = min(dick.values())
print("minletval=",minletval)
minlet=[]
for letter in dick:
    if dick[letter]==minletval:
        minlet.append(letter)
percentage=minletval/len(unique)*100
print("Letters which occur in least number of words are: ",end="")
for i in minlet:
    print(i,end=" ")
print("\nThe number of times they occur in different words from the text is: ",minletval)
print("Number of unique words in the text is: ",len(unique))
print("percentage of occurence is: %.2f procent" %percentage)