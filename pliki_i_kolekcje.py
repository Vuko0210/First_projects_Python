plik = open("test.txt", 'a', encoding='utf-8')
#if plik.writable():
#    plik.write(input("Wprowadz tekst: ")+ "\n")
plik.close()
#plik = open("test.txt", 'r', encoding='utf-8')
#print(plik.read())
###########################
slownik={1:"Poniedzialek", 2:"wtorek",7:"niedziela"}
print(slownik[2])
###########################
krotka=(2, 4, 6, 16, 32, 64, 64)
print(krotka[3])    #nie można modyfikować elementów krotki