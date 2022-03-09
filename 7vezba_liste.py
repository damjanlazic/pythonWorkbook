# liste, pop metod
fruits = ['apple', 'banana', 'cherry', "nectarine"]

# pop(n) izbacuje iz liste element pod rednim brojem n, s tim da lista počinje od 0
# a vraća vrednost elementa koji je izbacio
# ako se ne unese nikakav parametar: pop(), onda izbacuje poslednji element

x = fruits.pop()
for i in fruits:
	print(i)

    
print("Izbacili smo: ", x)
