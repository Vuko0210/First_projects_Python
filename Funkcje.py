def funkcja_test(x):
    print(x+1)

funkcja_test(5)

def funkcja_test(x, y=1):   #przyrównanie oznacza domyślną wartość, którą można zmienić
    print(x+ y)

funkcja_test(5,4)
funkcja_test(5)

def funkcja(f, liczba): #przyjmuje jako argumenty funkcje i liczbe
    return f(liczba)
#################################
print(funkcja(lambda x: x*x, 5))    #lambda to funkcja której nie deklarujemy; może tylko 1 argument przyjąć

wyn= (lambda x: x*x)(3) #najpierw funkcja w pierwszym nawiasie potem argument w 2 nawiasie
print(wyn)

lam=lambda x: x*x
print(lam(4))
print(lam(8))
##################################################
liczby=[2, 10, 12, 15, 20, 25, 30, 35]
def funk(x):
    return x*2
wynik= map(funk, liczby)    #mapa
print(list(wynik))          #wyrzuca całą kolekcje zmienioną o określoną funkcje

wynik2= map(lam, liczby)
print(list(wynik2))

wynik3= filter(lambda x: x%2==1, liczby)    #filtr -> (pewien warunek w postaci funkcji, argumenty)
print(list(wynik3))                         #wyrzuca nam skrojoną liste co spełnia warunek
####################################################
def gen():          #tu mamy generator; generator ma yield zamiast return
    i=0
    while i<5:
        yield i
        i+=1
for i in gen():
    print(i)

print(list(gen()))

def parzyste(x):
    i=0
    while i <= x:
        if i%2==0:
            yield i
        i+=1
for i in parzyste(4):
    print(i)
print(list(parzyste(32)))
######################################

def decorator(func):
    def wrapper():
        print("------")
        func()
        print("------")
    return wrapper

def hello():
    print("Hello world")

hello=decorator(hello)
hello()

@decorator
def witaj():
    print("czesc")
witaj()