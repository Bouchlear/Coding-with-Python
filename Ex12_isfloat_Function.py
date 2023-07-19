#isfloat function
def isfloat(n):
	check = False
	for i in range(len(n)):
		if not(n[i].isdigit()):
			if (n[i]=='.' or n[i]==',') and check==False: 
				check=True
			else:return False
	return True
#Controle de Saisie
while True:
	poids = input("Entrer le poids en Kg: \t")
	if poids.isdigit():poids=int(poids);break
	print("*"*10,"Entrer la valeur en kg","*"*10)
while True:
	taille = input("Entrer la taille en m: \t")
	if isfloat(taille):
		taille = float(taille)
		if taille>0:break
	print("*"*10,"Entrer une valeur en Métre Superieur a 0","*"*10)
#Calculation
imc=poids/taille**2
if imc < 18.5:print("Insuffisance pondérale (maigreur)")
elif imc < 25:print("Corpulence normale")
elif imc < 30:print("Surpoids")
elif imc < 35:print("Obésité modérée")
elif imc < 40:print("Obésité sévere")
else:print("Obésité morbide ou massive")
