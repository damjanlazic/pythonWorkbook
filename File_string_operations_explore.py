# operacije sa stringovima iz fajla

ime=input("ime fajla: ")
fajl=open(ime,"r")

line=fajl.readline()
i=0
while line!="":
    print("red br. ",i,end=" ")
    print(len(line),end=" ")
    for j in range(0,len(line)):
        print(line[j],end="+")
#    print("\n")
    line=fajl.readline()
    i=i+1
fajl.close()
