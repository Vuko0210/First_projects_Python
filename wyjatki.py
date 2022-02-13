x=12
y=0

try:        #spróbuj coś zrobić
    print(x/y)      #jak dzielimy przez 0 to prubuje ale sie nie uda
    print("aaaa")   #i dlatego to sie nie wykonuje bo program stwierdził że to nie działa
except ZeroDivisionError:   #wyjątek dla 0
    print("Dzielisz przez 0")
finally:
    print("wykonuje się zawsze obojętnie czy mamy try czy except")
###########################################

def dzielenie(a, b):
    assert b != 0
    if b == 0: #sami wiemy jaki błąd ma wywalić
        raise ZeroDivisionError ("Dzielenie przez 0")   #opis błędu taki jaki nadaliśmy
    print(a/b)

dzielenie(2,0)