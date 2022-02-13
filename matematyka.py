#funkcje matematyczne
#   1. Kolejność wykonywania działań działa

print(5/2)      #normlne dzielenie
print(5 // 2)   #zwraca tylko liczbe całkowitą (czyli int)

print(5*2)      #mnożenie
print(5**2)     #potęgowanie

x=5
x -= 1  # nie działa ani x++ ani x-- ani nic w tym stylu
print(x)

a=input("podaj 1 liczbe: ")
b=input("podaj 2 liczbe: ")
print(a+b)                #zwróciło string, a nie dodawanie
print(int(a)+int(b))      #int() <- przekształna na int
# też może być float(a) + float(b)

print(4 == 4)   #True
print(4 == 2)   #False