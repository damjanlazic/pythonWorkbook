# from a data set get all the names used for both boys and girls in a selected year

year=int(input("Unesite godinu: "))
if year<1900 or year>2012:
    print("Burazeru, nemamo podataka za godinu ",year,". Samo od 1900. do 2012.")
else:
    try:
        fileGirls="/home/damjan/piton/BabyNames/" + str(year) + "_GirlsNames.txt"
        fileBoys="/home/damjan/piton/BabyNames/" + str(year) + "_BoysNames.txt"
        infBoys=open(fileBoys,"r")
        infGirls=open(fileGirls,"r")
        gnnames=[]
        bnames=[]
        gnames=[]
        for line in infBoys:
            line1=line.rstrip()
            lineL=line1.split()
            name=lineL[0]
            bnames.append(name)
        infBoys.close()
        
        for line in infGirls:
            line1=line.rstrip()
            lineL=line1.split()
            name=lineL[0]
            gnames.append(name)
        infGirls.close()

        for bn in bnames:
            for gn in gnames:
                if bn==gn:
                    gnnames.append(bn)
        print(gnnames)
    except:
        print("Brate mili, pa ti ni godinu nisi u stanju da uneseš...")