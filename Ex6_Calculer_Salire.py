sb=float(input("Saisir le salaire brut\t"))
sn=0
#Retirer les charges CSS du SB
if sb<=12000:
    sn=sb*0.94#sb-sb*0.0354-sb*0.0256 #sb*(1-0.0354-0.0256)
else:
    sn=12000*0.94 +(sb-12000)*0.98
 #Retirer l'IR du SB
if sb<=10000:
    sn=sn-sb*0.2056
else:
    sn=sn-(10000)*0.2056-(sb-10000)*0.1
print(f"le salaire net est : {sn}")

#print(12260-(10000)*0.2056-(3000*0.1))
"""************En Algo*******
var sb,sn:Reel
Debut
 ecrire "Entrez le salaire brut"
 lire sb
si (sb<=12000) alors
    sn <-- sb*0.94   //sb-sb*0.0354-sb*0.0256 #sb*(1-0.0354-0.0256)
sinon
    sn <-- 12000*0.94 +(sb-12000)*0.98
fin si
 //Retirer l'IR du SB
si (sb<=10000) alors
    sn <-- sn-sb*0.2056
sinon
    sn <-- sn-(10000)*0.2056-(sb-10000)*0.1
ecrire "le salaire net est :", sn
"""
