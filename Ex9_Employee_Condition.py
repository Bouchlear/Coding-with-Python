ir,sn,prime=0,0,500
while True:
	salaire=input("Saisir un salaire : \t")
	if salaire.isdigit():salaire=int(salaire);break
while True:
	type=input("employee ou commercial? : \t")
	if type=="employee" or type=="commercial":break
if type.lower()=="commercial":
	prime*=2
if salaire<2500:
	pass
elif salaire <=4166.66:
	ir=salaire*0.1-250
elif salaire<=5000:
	ir=salaire*0.2-666.66
elif salaire<=6666.66:
	ir=salaire*0.3-1166.66
elif salaire<=15000:
	ir=salaire*0.34-1433.33
elif salaire>15000:
	ir=salaire*0.38-2033.33
sn=salaire+prime-ir
print(f"le salaire net est: {sn}, ir = {ir}, prime = {prime}")
"""
Variables:
	Var salaire,prime,ir:Entier
	Var type:chaine
	Debut:
		prime <== 500
		Ecrire "saisir le salaire"
		Lire salaire
		Ecrire "saisir le type"
		Lire type
		si type = commercial Alors
			prime <== prime * 2
		fin si
		si salaire < 2500 Alors
			ir <== 0
		sinon si salaire <= 4166.66 Alors
			ir <== salaire*0.1-250
		sinon si salaire <= 5000 Alors
			ir <== salaire*0.2-666.66
		sinon si salaire <= 6666.66 Alors
			ir <== salaire*0.3-1166.66
		sinon si salaire <= 15000 Alors
			ir <== salaire*0.34-1433.33
		sinon si salaire > 15000 Alors
			ir <== salaire*0.38-2033.33
		Fin si
		Fin si
		Fin si
		Fin si
		Fin si
		Fin si
		sn <== salaire+prime-ir
		Ecrire "le salaire net est:",sn," ir = ",ir," prime = ",prime
		Fin algorithme"""
