print("EXERCICE 1")
myTable = [14, 3, 57, 13]
stockage = 0

print("Mon tableau est actuellement : ")
print(myTable)

#utilisation des fonctions pop et insert
stockage = myTable.pop()
myTable.insert(0, stockage)

print("Désormais, mon tableau est : ")
print(myTable)

print("=========================")
print("EXERCICE 2")

myTable = [14, 3, 57, 13]

for i in range(len(myTable)-1):
    if myTable[i] > myTable[i+1]:
        stockage = myTable[i]
        myTable[i] = myTable[i+1]
        myTable[i+1] = stockage
print(myTable)

print("=========================")
print("EXERCICE 3")

myTable = [14, 3, 57, 13, 26, 1, 47, 62]

for i in range(len(myTable)):
    #Parcour principal du tableau
    for f in range(len(myTable)-1):
        #Parcour du Tableau afin de ré-ordonner chaque "binome"
        if myTable[f] > myTable[f+1]:
            stockage = myTable[f]
            myTable[f] = myTable[f+1]
            myTable[f+1] = stockage

print(myTable)

#Exercice 4 :
#Le tri des bulles est considéré comme lent car il procède par "binome" de valeurs,
#La lecture du tableau se fait donc en de nombreuses étapes là où d'autres algorithme permettent un tri en une lecture


