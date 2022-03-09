# funkcija is_number() koja proverava da li je uneti string 
# broj i to koristeći unicode (tajlandski, kineski brojevi i sl.)
# skinuto sa https://www.pythoncentral.io/how-to-check-if-a-string-is-a-number-in-python-including-unicode/

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

a=input("unesi nešto: ")
if is_number(a)==True :
    print(a, " je broj!")
else:
    print(a, "nije broj!")
print(float(a))