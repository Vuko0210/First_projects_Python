print(", ".join(["a","b","c"])) #rozdzielenie
print("Hello word!".replace("Hello","Hi"))  #zamień
print("To jest zdanie".startswith("To"))    #czy zdanie zaczyna się od ciągu "To"; true lub false
print("To jest zdanie".endswith("."))       #to samo co wyżej tylko że kończy
print("j" in "To jest zdanie")              #czy j jest w zdaniu
print("To jest zdanie".upper())
print("To jest zdanie".lower())
print("---------------------------------")
lista=[10, 20, 25, 35, 40]
lista2=[10, 20, 26, 36, 40]

if all([i%2==0 for i in lista2]):
    print("wszystkie parzyste")

if any([i%2==1 for i in lista]):
    print("chociaż jeden nieparzysty")