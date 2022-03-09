# exploring dictionary functions and tricks
from collections import OrderedDict
 
dict0= {"kratko":2,"krotko":0,"štrči":9,"šaka":5,"zebra":7,'ćure':'10','čiča':'9','ćamil':'15','ćata':'2','drčan':'32', "drama": "23"}
dict1 = sorted(dict0.items())
#print(dict)
#print(dict1)
#print(OrderedDict(dict1)) #nije mi jasno šta tačno radi ovaj OrderedDict
#novidict={}
novidict=dict((x,y) for x,y in dict1)
print(novidict)
