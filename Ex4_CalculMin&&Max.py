min=int(input("Saisir une valeur"))
for i in range(9):
    val=int(input("Saisir une valeur"))
    if val<min:
        min=val
print(f"le minimum est : {min}")