import json
import random
import datetime
"""Compteurs=[{"numCompteur":3000,"typeCompteur":"ordinaire","zoneCompteur":"zone1","dateInstallation":"01/02/2020","valeurEnregistré":100,"valeurAnterieur":60,"Suppression":0},
            {"numCompteur":3001,"typeCompteur":"ordinaire","zoneCompteur":"zone2","dateInstallation":"01/02/2021","valeurEnregistré":120,"valeurAnterieur":60,"Suppression":0}
             ];
with open("listCmpt.json","w") as file:
    json.dump(Compteurs,file)
print("Bien sérialisé !!!!!!!!")"""

#********************************Question1 : Ajouter****************************
DicoType={0:"ordinaire",1:"industriel"}

def Ajouter(path):
    listComp = None
    file=open(path,"r")
    listComp = json.load(file)
    file.close()
    c={}
    c["numCompteur"]=3000 if len(listComp)==0 else listComp[-1].get("numCompteur")+1
    indexType=random.randint(0,1)
    c["typeCompteur"]=DicoType.get(indexType)
    indexZone = random.randint(1, 20)
    c["zoneCompteur"] = "zone{0}".format(indexZone)
    while True:
        try:
            strDate=input("Entrez une date valide (dd/mm/yyyy) : ")
            c["dateInstallation"]=datetime.datetime.strptime(strDate,"%d/%m/%Y")
            c["dateInstallation"]=datetime.datetime.strftime( c["dateInstallation"],"%d/%m/%Y")
            break
        except Exception as ex :
            print(ex)
            print("Format date est invalide (dd/mm/yyyy) !!!")
    c["valeurEnregistré"]=0
    c["valeurAnterieur"]=0
    c["Suppression"]=0
    listComp.append(c)
    #print(listComp)
    file=open(path,"w")
    listComp = json.dump(listComp,file)
    file.close()
    print("Bien ajouté !!!!!!!!")

Ajouter("listCmpt.json")





















