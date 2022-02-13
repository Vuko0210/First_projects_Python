#podstawowe elementy języka python
print("Hello", "world "*5)

#nie podajemy typu danych
zmienna1 = 5
print(zmienna1)
zmienna1 = "Hello"
print(zmienna1)

#input() pobieramy dane od użytkownika
zmienna2=input("imie?: ") #input też wyrzuca tekst, ale wie że musi czekać na odp zwrotną
print("Cześć "+ zmienna2)
print("Cześć", zmienna2)

zmienna3 = 5
if zmienna1==5 and zmienna3 > 5:
    print("ok")

i=1
while i<5:
    print(i)
    i+=1
print("Koniec pętli")