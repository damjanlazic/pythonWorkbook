# dodela
# uvozimo copy modul zbog deepcopy, za ove ostale ne treba
import copy

def dodela(prc):
    # dva načina da se napravi kopija varjable tipa dictionary, 
    # a da ne dobiješ dva pokazivača na isti objekat
    dupli=prc.copy()
    dup2=dict(prc)
    for key in dup2:
        dup2[key]=2
        dupli[key]=1
    print("prc= ",prc)
    print("dupli= ",dupli)
    print("dup2= ",dup2)
# kada imamo kompleksne strukture tipa lista u listi ili lista u recniku, koristimo copy.deepcopy(var)


def main():
    recnik ={"A":5,"B":10,"C":15}
    dodela(recnik)
    recnikFC={"A":[5,6,7],"B":[10,20,30],"C":[15,30,45]}
    kopi=recnikFC.copy()
    deepkopi=copy.deepcopy(recnikFC)
    
# izvrsene promene dole će uticati i na recnikFC i na kopi, ali ne i na deepkopi    
    for sl in recnikFC:
        for i in range(0,3):
            recnikFC[sl][i]=0



    print("recnikFC=",recnikFC)
    print("kopi=",kopi)
    print("deepkopi=",deepkopi)
#    rec2=dict(recnik)
 #   rec3=recnik.copy()
 #   for key in rec2:
 #       rec2[key]=2
 #       rec3[key]=3
    print("main...recnik=",recnik)
 #   print("main...rec2=",rec2)
  #  print("main...rec3=",rec3)

main()
