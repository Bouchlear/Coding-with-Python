def isFloat(n):
	check = False
	for i in range(len(n)):
		if not(n[i].isdigit()):
			if (n[i]=='.' or n[i]==',') and check==False:
				check=True
			else:return False
	return True
hcd = []
def remplir(hcd):
	while True:
		v={}
		while True:
			identifiant = input("saisir l'identifiant: \t")
			if identifiant.isdigit():
				val = int(identifiant)
				if val not in [x.get(id) for x in hcd]:
					v["id"] = val
					break
		v["libelle"] = input("saisir la libelle: \t")
		while True:
			montant = input("saisir le montant: \t")
			if isFloat(montant):
				montant = float(montant)
				v["montant"]=montant
				break
		while True:
			statut = input("saisir le statut : \t")
			if statut.lower() in ["en cours", "achevé"]:
				v["statut"] = statut
				break
		hcd.append(v)
		choix = input("Entrer un autre element? o/n")
		if choix.lower() not in ["o","oui"]:
			break
def afficher(t):
	for i in t:
		print(i)

"""def afficherFiltré(t):
	for i in t:
		if i["statut"].lower() == "en cours":
			print(i)"""

def affichageFiltré(t):
	for x in [y for y in t if y.get("statut").lower() == "en cours"]:
		print(x)
def montantGlobal(t):
	return sum([x.get("montant") for x in t])
def modifier(t):
	while True:
			identifiant = input("saisir l'identifiant: \t")
			if identifiant.isdigit():
				identifiant=int(identifiant)	
	while True:
		montant = input("saisir le montant: \t")
		if isFloat(montant):
			montant = float(montant)
	for x in t:
		if x.get("id") == identifiant:
			x["montant"] = montant
def insert(t):	
	v={}
	while True:
		identifiant = input("saisir l'identifiant: \t")
		if identifiant.isdigit():
			val = int(identifiant)
			if val not in [x.get(id) for x in hcd]:
				v["id"] = val
				break
	v["libelle"] = input("saisir la libelle: \t")
	while True:
		montant = input("saisir le montant: \t")
		if isFloat(montant):
			montant = float(montant)
			v["montant"]=montant
			break
	while True:
		statut = input("saisir le statut : \t")
		if statut.lower() in ["en cours", "achevé"]:
			v["statut"] = statut
			break
	j=0
	while t[j]["id"] < v.get("id"):
		j+=1
	t.insert(j,v)

