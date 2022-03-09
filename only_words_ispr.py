# remove punctuation marks from a string, identify the words
# return a list of words

"""
So called CamelBack or Kebab case naming is what you are currently using. While it's not a mistake,
functions_with_underscores are more common. What definitely is a mistake is naming functions and methods with
capital letters. Those are reserved for class names. You can still use upper case for other words, like onlyWords().

When assigning values to variables use spaces around the = sign, like this:

wordlist = line.split()

No spacing is used when calling a function with explicit declaration of arguments:

some_variable = some_function(argument_1=False, argument_2=[])

If you are going to have data that is going to be repeated throughout your code assign it to a variable
before any fuctions are called. Like this:

SPECIAL_CHARACTERS = {"(","!",".",",",";",":","?","-","\"","\n","\'","\t","\ufeff"," "}
LETTERS = "abcdefghijklmnopqrstuvwxyz"

So the code can look like this:
if word[0] in SPECIAL_CHARACTERS:
    word = word[1:len(word)-1]

Use all upper case names for variable that will be constants used by other functions and methods.

"""
def OnlyWords(line):
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
def OnlyWords2(line):
    wordlist=line.split()
    nwordlist=[]
    print(wordlist)
    for word in wordlist:
        marks=True
        print(word,": ",len(word))
        while marks==True and len(word)>0:
            marks=False
            try:
                if word[0] not in "abcdefghijklmnopqrstuvwxyz":
                    word=word[1:len(word)-1]
                    marks=True
                    print("if word[0]...word=",word)
                if word[len(word)-1] not in "abcdefghijklmnopqrstuvwxyz":
                    word=word[0:len(word)-1]
                    marks=True
            except:
                if len(word)==1 and word not in "abcdefghijklmnopqrstuvwxyz":
                    
                    word=""
                elif len(word)<1:
                    word="@ERROR: "+ str(len(word))
                    marks==False
                else:
                    word="@ERROR:"+word  
                    marks=False  
                    
        nwordlist.append(word)
    return nwordlist    
def proba():
    unos="Baba sera mnogo kenja, a pritom dolazi do zagađenja! Nemoj da si srao!\nI can't take this bullshit anymore!\nJust won't prepare..."
    listareči=unos.split()
    reč="govance"
#    print(reč[1:6])
#    print(reč[6])
#    print(listareči)
    print(OnlyWords2(unos))
proba()
