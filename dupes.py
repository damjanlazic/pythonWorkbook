# dupes čita ceo faj odjednom i onda ispisuje poslednjih 10 redova
# inače potpuno neekonomično, radi još sporije od dupef.py

import sys

if len(sys.argv)!=2:
    print("Petre, IME dedino!")
    quit()

try:
    redova=0
    count=0
    fajl=open(sys.argv[1],"r")
    svesve=fajl.read()
    for i in svesve :
        if i=="\n":
            redova=redova+1
    for j in svesve:
        if j=="\n":
            count=count+1
        if redova-10<=count:
            print(j,end="")
#    print("redova=",redova)
#    print(svesve)

except IOError:
    print("pa nešto se sjebalo... možda si nepismen?")

