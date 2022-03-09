# sum a list of numbers ignoring the non numeric input

print("Unosi brojeve, kad završiš samo pritini ENTER")

line= input("broj= ")
sum=0
while line!="":
    try:
        a=float(line)
        sum=sum+a
    except:
        print("treba broj da uneseš imbecilu!")
    line=input("broj= ")

print("Zbir brojeva koje ste uneli je: %.2f" %sum)
