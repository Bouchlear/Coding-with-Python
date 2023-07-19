"""
Var age,ancienneté:entier
Var salaire,indemnité:Reel
Debut:
	Ecrire "Entrer l'age"
	Lire age
	Ecrire "Entrer le Salaire"
	Lire salaire
	Ecrire "Entrer l'ancienneté"
	Lire ancienneté
	indemnité <=== 0
	Si anciennete >= 1 ET anciennete < 10 Alors
	indemnité <== ancienneté * (salaire/2)
	Sinon Si anciennete >= 10 Alors
	indemnité <== ancienneté * salaire
	Fin si
	Fin si
	Si age > 45 Alors
		Si age < 50 Alors
			indemnité <=== indemnité + salaire * 2
		Sinon 
			indemnité <=== indemnité + salaire * 5
		Fin si
	Fin si
	Ecire "l'indemnité est", indemnité"""

while True:
	age = input("saisir l'age: \t")
	if age.isdigit():age=int(age);break
while True:
	salaire = input("saisir le salaire: \t")
	if salaire.isdigit():salaire=int(salaire);break
while True:
	ancienneté = input("saisir l'ancienneté: \t")
	if ancienneté.isdigit():ancienneté=int(ancienneté);break
if ancienneté >= 1 and ancienneté < 10 :
	indemnité = ancienneté * (salaire/2)
elif ancienneté >= 10 :
	indemnité = ancienneté * salaire
if age > 45:
	if age < 50:
		indemnité = indemnité + salaire * 2
	else:
		indemnité = indemnité + salaire * 5
print(f"l'indemnité est :{indemnité}")