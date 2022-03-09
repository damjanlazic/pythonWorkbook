# remove punctuation marks from a string, identify the words
# return a list of words

import copy



def onlyWords(line):
    wordlist=line.split()
    nwordlist=[]
    print(wordlist)
    for word in wordlist:
        marks=True
        print(word,": ",len(word))
        while marks==True and len(word)>0:
            marks=False
            try:
                if word[0] in {"(","!",".",",",";",":","?","-","\"","\n","\'","\t","\ufeff"," "}:
                    word=word[1:len(word)-1]
                    marks=True
                    print("if word[0]...word=",word)
                if word[len(word)-1] in {")","!",".",",",";",":","?","-","\"","\n","\'","\t","\ufeff"," "}:
                    word=word[0:len(word)-1]
                    marks=True
            except:
                if len(word)==1 and word in {"!",".",",",";",":","?","-","\"","\n","\'","\t","\ufeff"," "}:
                    
                    word=""
                elif len(word)<1:
                    word="@ERROR: "+ str(len(word))
                else:
                    word="@ERROR:"+word  
                    marks=False                      
        nwordlist.append(word)
    return nwordlist    


def onlyWords2(line):
    LETTERS="abcdefghijklmnopqrstuvwxyz"
    PMARKS="\"!?';,:.()\t\ufeff"


    wordlist=line.split()
    nwordlist=[]
#    print(wordlist)
    for word in wordlist:
        
        marks = True
        while marks == True:
            oldword = word
#            print("u whileu: word= ",word)
            marks = False
            for i in PMARKS:
                word = word.strip(i)
#                print("u foru, word=", word)
            if oldword != word :
                marks = True
#        word=word.lower()
#        print(word,": ",len(word))
        nwordlist.append(word)
    return nwordlist    

def proba():
    unos="Baba sera mnogo kenja, a pritom dolazi do zagađenja! Nemoj da si srao!\nI can't take this bullshit anymore!\nJust won't prepare..."
    listareči=unos.split()
#    reč="govance"
#    print(reč[1:6])
#    print(reč[6])
#    print(listareči)
    print(onlyWords2(unos))
# proba()
