# iz zbirke preko 200 fajlova gde su po godinama izlistana imena najpopularnijih imena
# za dečake i devojčice sa brojem takvih imena za bebe u toj godini,
# izvući najpopularnija imena iz svih godina, bez ponavljanja

def LoadAndAdd(imef,imena):
    fajl=open(imef,"r")
    line=fajl.readline()
    fajl.close()
    linepart=line.split()
    ime=linepart[0]
    if ime not in imena:
        imena[ime]=1
    else:
        imena[ime]=imena[ime]+1


def main():

    muškaimena={}
    ženskaimena={}
    for godina in range(1900,2013):
        boysfname="/home/damjan/piton/BabyNames/"+str(godina)+"_BoysNames.txt"
        LoadAndAdd(boysfname,muškaimena)
        girlsfname="/home/damjan/piton/BabyNames/"+str(godina)+"_GirlsNames.txt"
        LoadAndAdd(girlsfname,ženskaimena)

    msort=sorted(muškaimena.items(),key = lambda kv:(kv[1], kv[0]))
    žsort=sorted(ženskaimena.items(),key = lambda kv:(kv[1], kv[0]))
    
    print("\nMuška imena\tputa na prvom mestu\n")
    
    for (x,y) in msort:
        print("%12s \t %2i" %(x, y))
    print("\nŽenska imena\tputa na prvom mestu\n")   
    for (x,y) in žsort:    
        print("%12s \t %2i" %(x, y))

main()