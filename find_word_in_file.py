# find a word in a file
def word_in_file_list():

    fajl=open("words.txt","r")
    wordlist=[]
    for word in fajl:
        word=word.lower().rstrip()
        wordlist.append(word)
    x="small"
    if x in wordlist:
        print("ima!")
    else:
        print("nema!")

def word_in_file_set():

    fajl=open("words.txt","r")
    wordlist=set()
    for word in fajl:
        word=word.lower().rstrip()
        wordlist.add(word)
    x="zip"
    if x in wordlist:
        print("ima!")
    else:
        print("nema!")

word_in_file_set()