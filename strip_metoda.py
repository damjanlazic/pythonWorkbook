LETTERS="abcdefghijklmnopqrstuvwhyz"
word="\uefeffuck! \n"
PM="\uefef\n !?,.;:-()\""

for i in PM:
    word=word.strip(i)
    print("#"+word+"#")

reč="!grrrr\n"
if reč[0] not in LETTERS:
    zn=reč[0]
    reč=reč.replace(zn,"")
print(reč)

line="I tako ja jeBeno dođem malo do JEBENOG grada, kad tamo VELIKA jeBenA gužva!"
sword="jeben"
asterisk=""
while sword in line.lower():
    ps=line.lower().find(sword)
    pravisword=line[ps:ps+len(sword)]
    for i in range(0,len(sword)):
        asterisk=asterisk+"*"
    line=line.replace(pravisword,asterisk)
print(line)
