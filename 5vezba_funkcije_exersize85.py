# excersize 85: function to Convert an integer to its ordinal number
# ordinal numbers are first, second, third...
# ali ovo ćemo uraditi na srpskom

def ordinarni(broj) :
    try:
        br=int(broj)
        if br==1 :
            vr="prvi"
        elif br==2 :
            vr="drugi"
        elif br==3 :
            vr="treći"
        elif br==4 :
            vr="četvrti"
        elif br==5 :
            vr="peti"
        elif br==6 :
            vr="šesti"
        elif br==7 :
            vr="sedmi"
        elif br==8 :
            vr="osmi"
        elif br==9 :
            vr="deveti"
        elif br==10 :
            vr="deseti"
        elif br==11 :
            vr="jedanaesti"
        elif br==12 :
            vr="dvanaesti"
        else :
            vr="Pa dobro šta si mislio da možeš da uneseš baš bilo koji broj!\
                \nUnesi bre nešto od 1 do 12!"
    except :
        vr="Jesi razmišljao da radiš u školi?, tu je već sve sjebano \
            pa ne možeš toliko da se istakneš!"

    return(vr)
try:
    a=input("Unesi broj (u ciframa) od 1 do 12: ")
    br=int(a)
    while a!="" :
        print("To je ", ordinarni(br)," kreten za danas!")
        a=input("Unesi broj (u ciframa) od 1 do 12: ")
        br=int(a)
except :
    print("Jesi li razmišljao da radiš u školi? \ntu je već sve sjebano \
pa ne možeš toliko da se istakneš!")


