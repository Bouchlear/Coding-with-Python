import csv 
data = [['ID', 'Nom', 'Age', 'Taille'],
        ['1', 'Walid', '19', '180'],
        ['2', 'Najib', '30', '185'],
        ['3', 'Majda', '27', '175']]

#write in csv file 

"""with open("data.csv", "w") as datafile:
    
    writer = csv.writer(datafile)

    for ligne in data: 
        writer.writerow(ligne)"""


#read from csv file  as lists

"""with open("data.csv", "r") as listfile:
    reader = csv.reader(listfile)

    for ligne in listfile:
        print(ligne)"""



#read from csv file ad dict 
with open("data.csv", "r") as F:
    reader = csv.DictReader(F)

    for ligne in reader:
        print(ligne)






    