while True:
	c=input("Saisir la consommation: \t")
	if c.isdigit():c=int(c);break
m=0
if c <= 80:
	m = 0.8 * c
elif c<=200:
	m = 0.8 * 80 + 1.5 * (c-80)
else:
	m = 0.8 * 80 + 1.5 * (c-80)
print(round(m*1.2,2))


"""
Variables :
	var c,m : Entier
	Debut:
		Ecrire "Saisir le consommation"
		Lire c
		m <== 0
		si c <= 80 Alors
			m <== 0.8 * c
		sinon si c <= 200 Alors
			m <== 0.8 * 80 + 1.5 * (c-80)
		sinon 
			m <== 0.8 * 80 + 1.5 * (c-80)
		Fin si
		Fin si
		Fin si
		m <== m * 1.2
		Ecrire "Le montant a payer est ",m
		Fin Algorithme"""
