def zad2_27():
    # Zadanie 2 strona 27
    # Wyświetl w konsoli dokładnie 100 razy każdą literkę twojego imienia oddzielnie.

    imie = 'Fistaszek'
    for i in range(0,len(imie),1):
        for j in range(0,100,1):
            print(imie[i],j+1)


def zad4_30okolo():
    # Zadanie 4 strona któraś tam około 30
    # Napisz program, który wypisuje na konsoli 10 razy napis, który wcześniej zostanie z niej pobrany.

    def napisz(x):
        for i in range(1,10,1):
            print(x, i)

    tekst = input("Podaj dany tekst: ")
    print(napisz(tekst))




def zad9_39():
    # Zadanie 9 strona 39
    # Napisz program, który pobiera od użytkownika liczbę z przecinkiem, którą następnie wyświetla w konsoli jako liczba całkowita.

    wejście = (input("Podaj liczbe zmienno przecinkową: "))
    wejście = float(wejście)
    print("Liczba jako int",round(wejście))
    print("Liczba jako float", float(wejście))
    # print(round(3.14))

def zad25_58():
    # Zadanie 25 strona 58
    # Napisz program, który odlicza od 1 do 5, wypisując liczby co sekundę.
    import time
    import os


    os.system("cls")
    for i in range(1,5,1):

        print(i)
        time.sleep(1)
        os.system("cls")


def zad27_59():
    # Zadanie 27 / strona 59
    # Napisz program, który pobierze liczbę sekund od użytkownika i jeśli użytkownik podał liczbę mniejszą niż 10, zatrzyma się na tak długo, jak liczbę użytwkonik wpisał. Jeśli podana liczba jest większa lub równa 10, to program poinformuje, że nie będzie tyle czekać.

    import time

    czas = int(input("Podaj liczbe sekund: "))

    if czas > 10:
        print("Nie będę tyle czekać")
    elif czas < 10:
        for i in range(1,czas + 1,1):
            print(i)
            time.sleep(1)



# funkcja gmtime w bibliotece time oraz typ struct_time
def zad28_62():
    # Zdanie 28 strona 62
    # Napisz program który wypisuje aktualną godzinę, minutę i sekundy.
    import time
    czas = time.gmtime()

    # 0 - rok
    # 1 - miesiąc
    # 2 - dzień
    # 3 - godzina
    # 4 - min
    # 5 - sek

    print("Aktualna godzina to :",czas[3] + 1,":",czas[4],":",czas[5])

zad28_62()
def zad35_69():
    # Zadanie 35 strona 69
    # Napisz program który zadaje użytkonikowi trzy pytania. Jeśli użytkoqwnik odpowie poprawnie, to daj mu punkt,a w przeciwynym przypadku informuje, że nie zna odpowiedzi. Na końcu wyświetla sumę punktów.

    # 1. Ile to będzie 7 - 2 * 3?
    # 2. Autor Akademii Pana Kleksa.
    # 3. Jaki jest typ wartości 3.12    
    
    questions = ["Ile to będzie 7 - 2 * 3?","Autor Akademii Pana Kleksa","Jaki jest typ wartości 3.12"]
    



    print(questions[0])
    point = 0
    answer = input()
    if answer == "1" or answer == 1 or answer == "one" or answer == "One":
        print("Good Job")
        point = point + 1 
    else:
        print("Not this time")

      
    print(questions[1])
    answer1 = input()

    if answer1 == "Jan Brzechwa" or answer1 == "jan brzechwa" or answer1 == "JAN BRZECHWA" or answer1 == "Jan brzechwa":
        print("Good job")
        point = point + 1


    print(questions[2])
    answer2 = input()

    if answer2 == "Float" or answer == "float":
        print("Good job")
        point = point + 1

    print("You have points: ",point)



# // ! ||--------------------------------------------------------------------------------||
# // ! ||                               Zadanie 3 strona 71                              ||
# // ! ||--------------------------------------------------------------------------------||

def zad37_71():
#     # Zadanie 3 strona 71
#     # Niech a będzie równe zmienną równą 3.
#     # Niech b będzie trzy razy większe niż a.
#     # Napisz program który losuje liczbę z przedziału a do b.
    import random
    a = 3
    b = 3 * a

    for i in range(0,10,1):
        print(random.randint(a,b))



# ! ||--------------------------------------------------------------------------------||
# ! ||                              Zadanie 41 strona 73                              ||
# ! ||--------------------------------------------------------------------------------||

def zad41_73():
    # Zadanie 41 strona 73
    # Napisz grę w papier kamień nożyce. Użytkownik wpisuje papier, kamień lub nożyce. Następnie prorgam losuje dla siebie papier,kamień albo nożyce jako liczbe od 1 do 3 i wynik tego losowania jest wypisywan w konsoli. Program za pomocą warunków wypisuje, kto wygrał.

    import random



    # items = ["papier","kamień","nożyce"]

    print("Wybierz papier, kamień albo nożyce \n 1.Papier \n 2.Kamień \n 3.Nożyce")
    x = int(input())

    komputer = random.randint(1,3)

    if x == 1:
        if komputer == 2:
            print("Komputer wybrał kamień a ty papier \n Wygrałeś")
        elif komputer == 3:
            print("Komputer wybrał nożycę  a ty papier\n Przegrałeś")
        elif komputer == 1:
            print("Papier kontra papier a ty papier \n Remis")

    
    elif x == 2:
        if komputer == 1:
            print("Komputer wybrał papier  a ty kamień\n Przegrałeś")
        elif komputer == 2:
            print("Kamień kontra kamień  a ty kamień \n remis")
        elif komputer == 3:
            print("Komputer wybrał nożyce a ty kamień \n Wygrałeś")

    elif x == 3:
        if komputer == 1:
            print("Konmputer wybrał papier a ty nożyce \n wygrałeś")
        elif komputer == 2:
            print("Komputer wybrał kamień a ty nożyce \n Przegrałeś")
        elif komputer == 3:
            print("Nożyce kontra nożyce a ty nożyce \n Remis")





# ! ||--------------------------------------------------------------------------------||
# ! ||                              Zadanie 60 strona 99                              ||
# ! ||--------------------------------------------------------------------------------||

def zad60_99():
    # Zadanie 60 strona 99
    # Napisz prorgam który odliczba w konsoli od 1 do 8, z użyciem pętli while

    import time
    a = 1
    while a < 9:
        print(a)
        time.sleep(1)
        a = a + 1

# ! ||--------------------------------------------------------------------------------||
# ! ||                              Zadanie 7 strona 105                              ||
# ! ||--------------------------------------------------------------------------------||

def zad7_105():
    # Zadanie 7 strona 105
    # Napisz program, który w konsoli wyświetla piramidę z dziewięciu liczb o takim kształcie.
    # 1
    # 22
    # 333
    # 4444
    # 55555
    

    x = int(input("Podaj wielkosc tej piramidki: "))
    for i in range(0,x+1,1):
        print(str(i) * i)

