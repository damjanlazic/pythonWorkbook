# explore lambda function

#najprostiji lambda izrazi
def prostelambde() :
    for i in range(1,101) :
        print((lambda x: round((100/x),2))(i),end="\t")
        print((lambda z: z*z)(i))
    
def lambdeliste():
    lista=[]
    for i in range(1,101):
        lista.append(i)
#    parni=[]
    print(list(filter(lambda x: x%2==0, lista) ))
    print(list(filter(lambda y: y%3==0, lista) ))
    
lambdeliste()

#prostelambde()
    
