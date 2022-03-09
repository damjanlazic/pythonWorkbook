# convert a decimal number to binary using recursion

BROJ=""

def dec_binary(num):
    if num != 0 :
        digit = int(num % 2)
        num = num // 2
# da bi promenio globalnu promenljivu unutar funkcije, koristi se keyword global
        global BROJ
        BROJ = BROJ + str(digit)

        return dec_binary(num)
    else:
        print("Zadati broj u binarnoj reprezentaciji je: ")
        for i in range(len(BROJ)-1,-1,-1):
            print(BROJ[i],end = "")
        print("\n")

def main():

    no = float(input("unesi decimalan broj: "))
    dec_binary(no)

main()
