n=int(input("Saisir un nombre de départ : "))
f=1
for i in range(1,n+1): #for i in range(n,0,-1):
    print(f"{f}*{i}")
    f=f*i
print(f"fact({n}) = {f}")

"""************En Algo ************
var n,f,i:Entier
Debut
ecrire "Saisir un nombre de départ : ")
lire n
f <- 1
pour i=1 : n pas de 1 //pour i=n : 1 pas de -1
    ecrire f,"*",i
    f <- f*i
fin Pour
ecrire "fact(",n,") = ",f
"""