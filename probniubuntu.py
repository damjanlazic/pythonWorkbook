# samo da vidimo da li ovo radi...
print("zdravo svete!")
c=int(input("Unesi neki ceo broj:"))
print("Prosti brojevi od 1 do ",c," su:")
for i in range(1,c+1):
    prost=True
    for n in range(2,i):
        if i%n==0:
            prost=False
             
    if prost == True:
        print(i)
