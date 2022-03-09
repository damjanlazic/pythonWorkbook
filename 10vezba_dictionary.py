def engleskosrpski(materijal,engleskareč):
    prevod=[]
    for reč in materijal:
        if materijal[reč]==engleskareč :
            prevod.append(reč)
    if prevod==[]: prevod.append("Zadata reč ne postoji u rečniku")
    return prevod
def dodajreč(rečnik):
    print("Dodajmo nove reči u rečnik")
    sreč="!"
    while sreč!="":
        sreč=input("Srpski: ")
        ereč=input("Engleski: ")
        rečnik[sreč]=ereč


def main() :
    rečnik={"govno" : "shit", "sranje": "shit", "jabuka": "apple", "pita" : "pie",\
        "kruška" : "pear", "šljiva" : "plum", "breskva" : "peach"}
    print("tražimo reč shit: ", engleskosrpski(rečnik,"shit"))
    print("tražimo reč apple: ", engleskosrpski(rečnik,"apple"))
    print("tražimo reč pie: ", engleskosrpski(rečnik,"pie"))
    print("tražimo reč eagle: ", engleskosrpski(rečnik,"eagle"))
    reč=input("Unesite reč na engleskom: ")
    print("Prevod reči ",reč," na srpski je: ", engleskosrpski(rečnik,reč))
    reč=input("Unesi reč na srpskom: ")
    try:
        print("sa srpskog na engleski: ", reč, " -> ", rečnik[reč])
    except:
        print("Nema tražene reči!")
        
    dodajreč(rečnik)
    print(rečnik)



    

main()
