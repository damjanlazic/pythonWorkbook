"""
In this exercise you will write a program that redacts all occurrences of sensitive
words in a text file by replacing them with asterisks. Your program should redact
sensitive words wherever they occur, even if they occur in the middle of another
word. The list of sensitive words will be provided in a separate text file. Save the
redacted version of the original text in a new file. The names of the original text file,
sensitive words file, and redacted file will all be provided by the user.
You may find the replace method for strings helpful when completing this
exercise. Information about the replace method can either be found in your
textbook or on the internet.
For an added challenge, extend your program so that it redacts words in a case
insensitive manner. For example, if exam appears in the list of sensitive words then
redact exam, Exam, ExaM and EXAM, among other possible capitalizations.
"""
LETTERS="abcdefghijklmnopqrstuvwhyz"
# @param: filename where sensitive words are stored, returns: a set of sensitive words
def loadSensitive(filename):
    file = open(filename,"r")
    sensitive = set()
    for word in file:
        if word[0].lower() not in LETTERS: 
            word = word.replace(word[0],"")
        word = word.lower().strip()
        sensitive.add(word)
    file.close()
    sensitive.discard("")
        
    return sensitive

# @param: filename of a file to be censored, sensitive=set of sensitive words to censor
def seekandDestroy(filename,sensitive):
    fajl = open(filename,"r")
    czfilename = "cz" + filename
    czfajl = open(czfilename,"w")
    line = fajl.readline()
    while line != "":
        for sword in sensitive:
            while sword in line.lower():
                pos = line.lower().find(sword)
                actualsword = line[pos:pos+len(sword)]
                asterisk = ""
                for i in range(0,len(sword)):
                    asterisk = asterisk+"*"
                line = line.replace(actualsword,asterisk)

        czfajl.write(line)
        line = fajl.readline()
    fajl.close()
    czfajl.close()
    return czfilename

def main():
    fname = input("Unesi ime fajla za cenzuru: ")
    sname = "sensitive.txt"
    czfile = seekandDestroy(fname,loadSensitive(sname))
    czf = open(czfile,"r")
    line = czf.readline()

    while line != "":
        print(line.rstrip())
        line = czf.readline()
    czf.close()
    

if __name__ == "__main__":
    main()
