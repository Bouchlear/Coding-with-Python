"""while True:
    val = input("Saisir votre année de naissance :  valeur entiére entre 1900 et 2020  ")
    if val.isdigit()==True:
        birthYear=int(val)
        age=2020-birthYear
        print(f"Votre age est : {age} ans")
        break
"""
val1=input("Saisir le prix unitaire : ")
pos=val1.index('.')
pe=val1[0:pos];pd=val1[pos+1:]
if pe.isdigit() and pd.isdigit():
    prix=float(val1)
    print("Le prix est : ",prix)
else:
    print("Vous devez saisir une valeur réelle")






""""

qte=int(input("Saisir la quantité : "))
prixTotal=qte*pu
print(f"le prix total est : {prixTotal} DH")
"""



