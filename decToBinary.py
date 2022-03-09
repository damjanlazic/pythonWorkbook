# convert a decimal number to binary

def decBin(dnum):
    srem = ""
    binar = ""
    while dnum  != 0 :
        rem = dnum % 2
        srem = srem + str(rem)
        dnum = dnum // 2
    for i in range(len(srem)-1,-1,-1) :
        binar = binar + srem[i]
    return binar


print(decBin(29))