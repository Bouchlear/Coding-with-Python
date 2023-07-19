#Ex1
count=0
while True:
	n = input("saisir : \t")
	if n.isdigit():n=int(n);break
while n>1:
	if n%2==0:
		n/=2 # n = n/2
	else:
		n=3*n+1
	count+=1
	print(int(n),end=" ")
print()
print("le nombre de fois qu’il est nécessaire",count)


#Algo 
"""
Variables:
var n,count:Entier
Debut:
	Ecrire "Saisir une valeur:"
	Lire n
	tant que n>1 alors
		si n%2 == 0 Alors
			n <== n/2
		sinon
			n <== 3*n+1
		Fin si
		count <== count + 1
		Ecrire n," "
	Fin tant que
	Ecrire "le nombre de fois qu’il est nécessaire",count"""
