# compute the number of unique characters in a string 
# using a dictionary


str=" "
while str!="" :
    dchar={}
    str=input("Napiši nešto...")
    for ch in str:
        dchar[ch]=0
    for ch in str:
        dchar[ch]=dchar[ch]+1
    print("Vaša priča sadrži ukupno ", len(dchar), " različitih (znakova)")
    print(dchar)
    print("znakovi poređani po broju pojavljivanja, u rastućem poretku: ")

# ovo sortira dictionary po vrednostima (values), parametar f-je sorted : key služi da 
# se odredi na osnovu kog od dva elementa u dictionary treba da se sortira
# on ovde uzima pa sortira prvo na osnovu kv[1] tj. value(ovde brojevi), 
# pa onda na osnovu kv[0] tj. key (ovde slova)
    tupko=sorted(dchar.items(),key = lambda kv:(kv[1], kv[0]))
# ova gore operacija pravi tuple, a ja hoću da ga pretvorim u dictionary
# za to koristimo f-ju dict
    dct = dict((x, y) for x, y in tupko)
    print(dct)

    dcharkeysort={}
    for i in sorted(dchar):
        dcharkeysort[i]=dchar[i]

    print("Znaci/slova po abecednom redu ( sort by keys) :\n",sorted(dchar))
    print(dcharkeysort)


