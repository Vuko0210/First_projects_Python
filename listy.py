zmienna = 1
zmienna2= "ABC"

lista=[1,5,"abc"]   #indeksowanie od 0
print(lista)
print(lista[2])

lista[1]=8 #zmiana elementu, czyli ta dynamiczność
lista[0]="XD"
print(lista)
##############################
print(lista+["e","hhh",9])  #dodawanie listy
print(lista*3)              #mnożenie listy
print("Ilość elementów: ",len(lista))  #długosć listy
#############################
#tu takie zadanko żeby wyświetliły sie po kolei elementy listy
i=0
while i<len(lista):
    print(lista[i])
    i+=1
#można to też zrobić tak
print("drugi sposób:")
for x in lista:
    print(x)
#######################
lista.append("a")
print(lista)
lista.append(["w","k"])
print(lista)
print(lista[4][0])  #odwołujemy się do konkretnego elementu tej listy w liście
lista.insert(2,"qq")    #dołącz element
print(lista)
lista.remove(8)         #usuń element
print(lista)

lista2=[1,8,20,6,200,4,7]
print(min(lista2)," ",max(lista2))  #wartość min i max