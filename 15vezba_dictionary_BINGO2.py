# kad se stavi * uvoze se sve funkcije iz
from random import shuffle
from bingo import *
import copy

def checkBINGO(bingo):
    bnum={"B":0,"I":1,"N":2,"G":3,"O":4}
#    win=False
    l=[0,0,0,0,0]
    d=[0,0]
    j=0
    for key in bingo :
#        print(key)
#        print("bnum(key)=",bnum[key])
        vert=0
        j=0
        for i in bingo[key]:
            if bnum[key]==j : d[0]=d[0]+i
            if bnum[key]+j ==4 : d[1]=d[1]+i
            vert=vert+i
            l[j]=l[j]+i
            j=j+1
            
#        print("vert=",vert)
        if vert==0 : 
            return True
    for j in range(0,5):
        if l[j]==0: return True
    if (d[0]==0 or d[1]==0): return True
    return False

            
def playBINGO(card):

    nocalls=[]
    call=[]
    for i in range(1,76):
        call.append(i)    
#    print(call)
#    shuffle(call)
#    print("\n",call)
#    di=0
#    gi=75
    #kopija=card.copy()
    brigri=1000
    for n in range(0,brigri):
# ovde jedino copy.deepcopy() radi inače promene u dcard menjaju card, 
# zato što je kompleksna struktura: lista unutar rečnika
        dcard=copy.deepcopy(card)
        shuffle(call)
        #print("dcard=",dcard)
        #print("card=", card)
        #print("call=",call)
        i=0
        endwhile=False
        while (i < 75 and endwhile==False):
    
            for key in dcard :
                for j in range(0,5):                
                    if dcard[key][j]==call[i]:
                        #print("dcard[key]: ",dcard[key][j],"-> ", end="\t")
                        dcard[key][j]=0
                        #print("dcard[key]: ",dcard[key][j])
            if (checkBINGO(dcard)==True): 
                nocalls.append(i)
                endwhile=True  
                #print("WIN! dcard=",dcard)
                #print("nocalls= ", nocalls)
            #print("\ni= ",i)
            i=i+1     

    #print(card)
    #print(nocalls)
    return nocalls

def main():
#    d=realBINGO()
#    print(d)
#    d={"B":[1,3,6,9,13],"I":[22,17,24,30,21],"N" :[32,33,37,43,39],"G":[46,49,51,55,59],"O":[61,67,59,72,75]}
    d=realBINGO()    
    listing=playBINGO(d)
    suma=0
    n=0
    for i in listing:
        suma=suma+i
        n=n+1
    prosek=suma/n

    print("listing=", listing)
    print("d=", d)
    print("suma=", suma)
    print("br. igara=", n) 
    print("prosek=", prosek)

main()