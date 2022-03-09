# spellchecker (check all the words in a given file, 
# and report them if they are not in the list of words: words.txt)

from only_words import onlyWords2
#from only_words_bogdan import *

import sys

if len(sys.argv)!=2:
    print("Enter a filename as a command line parameter!")
    quit()
datafile=open("words.txt","r")
datawords=set()
for word in datafile:
    word=word.lower().rstrip()
    datawords.add(word)
datafile.close()
#print(datawords)

misspelled=set()
#print("Words in a given file are:")
fajl=open(sys.argv[1],"r")
line=fajl.readline()
while line!="":
#    words=onlyWords2(line.lower())
    words=onlyWords2(line.lower())
    for word in words:
        #print(word, end="\t")
        if word not in datawords:
            misspelled.add(word)
    line=fajl.readline()

print("Misspelled words are:")
for word in misspelled:
    print(word)


