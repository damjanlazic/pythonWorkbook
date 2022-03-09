# determine whether two entered strings are anagrams


def brslova(s1):
    d1={}
    d2={}
    for ch in s1:
        if ch in d1:
            d1[ch]=d1[ch]+1
        else:
            d1[ch]=1
    for k in sorted(d1):
        d2[k]=d1[k]
    print(d2)
    return d2

def permutations(stuff):
    import itertools

   # stuff = [1, 2, 3, 4]
    for L in range(0, len(stuff)+1):
        for subset in itertools.permutations(stuff, L):
            if len(subset)==len(stuff) : print(subset)

def prepareanagram(d):
    s=[]
    s1=""
    for ch in d:
        for j in range(0,d[ch]):
            s.append(ch)
            
    #print(len(s),"\n", s)

    #print(s1)
    return s


def dalijeanagram():
    st1=" "
    while st1 != "":

        st1=input("Unesi prvu rečenicu: ")
        if st1=="": break
        else:
            st2=input("Unesi drugu rečenicu: ")
            d1=brslova(st1)
            d2=brslova(st2)
            if d1==d2 :
                print("JESTE anagram!")
            else:
                print("Nije anagram")
            
def main():

    reč=input("Unesi reč: ")
    brs=brslova(reč)
    p=prepareanagram(brs)
    permutations(p)
    dalijeanagram()
main()