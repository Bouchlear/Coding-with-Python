rep='o'
while rep=='o':
    try:
    taille=float(input("Saisir la taille : (m) "))
    poids=float(input("Saisir le poids : (kg) "))
    except ex
    
    imc=round(float(poids)/float(taille)**2,2)
    print('votre imc est {}'.format(imc))
    rep=input("Voulez vous calculer l'imc d'une autre personne ? (o/n)")