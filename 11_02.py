def zad2_27():
    # Zadanie 2 strona 27
    # Wyświetl w konsoli dokładnie 100 razy każdą literkę twojego imienia oddzielnie.

    imie = 'Fistaszek'
    for i in range(0,len(imie),1):
        for j in range(0,100,1):
            print(imie[i],j+1)
# zad2_27()

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

# zad28_62()
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

def zad69_107():
    # Zadanie 69 strona 107
    # Napisz program, który tworzy 3 elementy tablicy jako losowe liczby od 1 do 80 następnie wpisuje liczby z tej tablicy i wyświetla je.
    import random


    tablica = [0,0,0]
    for i in range(0,3,1):
        tablica[i] =+  random.randint(1,80)

    for i in range(0,3,1):
        print(tablica[i])


def zad70_109():
    # Napisz program który prosi użytkownika o wpisanie ulubionych filmów dopóki użytkownik nie napisze Koniec. Następnie niech program wypisze wszsytkie wpisane filmy.
    # Zwróć uwagę, że Koniec jest z dużej litery.

    t = ['']
    print("Podaj film jakiś")
    i = 0
    input_user = ''
    while input_user != "Koniec":
        i = i + 1
        input_user = input()
        t.append(input_user)

    t.pop(0)
    t.pop(i-1)
    print(t)

# ! ||--------------------------------------------------------------------------------||
# ! ||                   Zadanie 73 Tworzenie Algorytmu Bąbelkowego                   ||
# ! ||--------------------------------------------------------------------------------||
    # Zadanie 73 Strona 111
    # Napisz algorytm sortowania bąbelkowego - jest to prosty algorytm sortujący. Pośród wszystkich algorytmów sortujących znajduje się on w grupie tych,którym sortowanie zajmuje najwięcej czasu. W przypadku naszych małych tablic będzie to jednak niezauważalne.
    
    # Algorytm bąbelkowy polega na tym, że tyle razy, ile tablica ma elementów (minus 1), wykonujemy następujące działanie dla elementów od pierwszego do przedostatniego: porównujemy kolejne elementy tablicy z tymi, które są po nich. Jeśli następny element jest większy, to zamieniamy go i jego poprzedni element miejscami.

    # | 8 | 5 | 10 | 1 |

    # Trzy razy będziemy porównywać po kolei pierwszy element z drugim, drugi z trzecim, a trzeci z czwartym.
    # Na początku sprawdzamy, czy 8 > 5? Tak, więc zamieniamy miejscami elementy.
    #     <-
    # | 5 | 8 | 10 | 1 |

    # Czy teraz 8 > 10? Nie, a więc zostaje.
    # | 5 | 8 | 10 | 1 |

    # Czy 10>1? Tak, więc zamieniamy miejscami.
    #             ->
    # | 5 | 8 | 1 | 10 |

    # I znowu czy 8>1? Tak więc.
    #        ->
    # | 5 | 1 | 8 | 10 |

    # I znowu czy 5>1>? Tak więc.
    #    ->
    # | 1 | 5 | 8 | 10 |
def zad73_111():
    # Definiowanie tablicy ze zemiennymi do posegregowania
    import random
    a = 0
    t = []

    while a < 10:               
        t.append(random.randint(1,100))
        a += 1

    print(t)


    a = 0   # Ponowne użycie zmiennej a w pętli while

    while a < len(t) - 1:           # pierwsza pętla
        b = 0                       # zmienna pomocnicza
        while b < len(t) - 1:       # druga pętla
            if t[b] > t[b+1]:       # warunek jeśli miejsce w talbicy b w t jest większa od b w t o jeden większa
                c = t[b]            # pomocnicza zmienna c która jest równa b w t
                t[b] = t[b+1]       # przypisanie wartości b w t do o jeden więcej
                t[b+1] = c          # przypisanie wartości b w t + 1 do c które było równe t[b]
            b += 1                # inkrementacja b o 1
        a += 1                 # inkrementacja a o 1
    print(t)             # wyświetlenie tablicy t
# zad73_111()             # odowłanie się do funkcji


def mojtest_1():
    import random
    c = ["!","@","#","$","%","^","&","*","(",")"]

    tab = []
    for i in range(0,9,1):
        tab.insert(i,c[random.randint(0,9)])

    print(tab)
# mojtest_1()
    


def zadtamto(): # Zadanie 74 strona 115
    import random
    c = ["!","@","#","$","%","^","&","*","(",")"]
    i = 0
    j = 0

    tab = [[],[]]
    for i in range(0,4,1):
        for j in range(0,4,1):
            tab.insert([[i],[j]],c[random.randint(0,8)])
            # TypeError: 'list' object cannot be interpreted as an integer ???

    print(tab)


def zad75_116():
    from progressbar import ProgressBar
    import time
    
    bar = ProgressBar(maxval=15)
    print("Wysyłam raport o błędzie...")
    bar.start()
    time.sleep(0.1)
    for i in range(1,15,1):
        time.sleep(0.2)
        bar.update(i)


def mini_gra():
    import random
    from progressbar import ProgressBar
    pkt = 0
    y = 0
    x = 0
    c = ["+","-","*"]
    bar = ProgressBar(maxval=6)
    bar.start()
    while True:
        y = random.randint(1,10)
        x = random.randint(1,12)
        akcja = str(c[random.randint(0,2)])
        if akcja == "+":
            print(y," " ,akcja," ",x," = ?")
            odp = str(y + x)
            odp_user = input("Jaki jest wynik? ")
            if odp == odp_user:
                pkt = pkt + 1
                bar.update(pkt)
                if pkt == 6:
                    print("Wygrałeś")
                    break
            else:
                pkt = pkt - 1
                bar.update(pkt)



        elif akcja == "-":
            print(y," " ,akcja," ",x," = ?")
            odp = str(y - x)
            odp_user = input("Jaki jest wynik? ")
            if odp == odp_user:
                pkt = pkt + 1
                bar.update(pkt)
                if pkt == 6:
                    print("Wygrałeś")
                    break
            else:
                pkt = pkt - 1
                bar.update(pkt)

        elif akcja == "*":
            print(y," " ,akcja," ",x," = ?")
            odp = str(y * x)
            odp_user = input("Jaki jest wynik? ")
            if odp == odp_user:
                pkt = pkt + 1
                bar.update(pkt)  
                if pkt == 6:
                    print("Wygrałeś")
                    break
            else:
                pkt = pkt - 1
                bar.update(pkt)
# mini_gra()



#// ! ||--------------------------------------------------------------------------------||
#// ! ||                                     PY GAME                                    ||
#// ! ||--------------------------------------------------------------------------------||
                
def zad77_121():
    import pygame
    x = 800
    window = pygame.display.set_mode([x,x])
    while True:
        pygame.display.set_caption("Hello World")


    # while True:
    #     pygame.display.set_caption("Hello World")
    # Nie robić tak komputer przestał działac
# zad77_121()

def zad77_121_2():
    import pygame
    import os
    x = int(input("Podaj wielkość x okna: "))
    y = int(input("Podaj wielkość y okna: "))

    okno = pygame.display.set_mode([x, y])
    os.system("pause")
    pygame.display.set_caption("Hello World")
   
# zad77_121_2()
    


def nonzad_122():   # Prostokąt pygame.draw.rect()
    import pygame
    import os
    okno = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("Primitywy")

    # Prostokąt
    pygame.draw.rect(okno, [255,255,255] , pygame.Rect(100,100,150,250))

    # Modyfikacja obrazu do wyświetlenia ekranie
    pygame.display.update()
    # Pętla główna
    while True:
        pygame.event.get() # obsługa ekranu
        os.system("pause") # pausa w konsoli cmd
        break              # wyłączenie programu, "złamanie pętli"

# nonzad_122()
    
def nonzad_124():

    import pygame
    import os


    # Okno
    okno = pygame.display.set_mode([800,800])
    pygame.display.set_caption("Primitywy II")


    # Prostokąt
    pygame.draw.rect(okno, [255,255,255] , pygame.Rect(100,100,150,250))
    # Prostokąt o kolorze 255,255,255 oraz znajduję się od 100,100 do 150,250

    # Koło 
    pygame.draw.circle(okno, [0,255,0], [400,300], 75)
    # Koło jest w kolorze 0,255,0
    # środek koła jest w 400,300 oraz ma promień o długości 75


    # Modyfikacja obrazu do wyświetlenia ekranie
    pygame.display.update()


    while True:
        pygame.event.get() # obsługa ekranu
        os.system("pause") # pausa w konsoli cmd
        break

# nonzad_124()
    

def nonzad_125():
    
    import pygame
    import os

    # Okno
    okno = pygame.display.set_mode([800,800])
    pygame.display.set_caption("Primitywy III")

    # Prostokąt
    pygame.draw.rect(okno, [255,255,255], pygame.Rect(100,100,150,250))
    # Prostokąt o kolorze 255,255,255 oraz znajdujący się od 100,100 do 150,250

    # Koło
    pygame.draw.circle(okno, [0,0,255], [300,400], 75)
    # Koło o kolorze 0,0,255 oraz znajdujący się w 300,400 o promieniu 75

    # Trójkąt (wielokąt)
    pygame.draw.polygon(okno, [255,0,0], [[175,175], [300,400],[300,0]])
    # Trójkąt który ma wierzchołki w tych trzech punktach


    # Aktualizacja ekranu
    pygame.display.update()


    while True:
        pygame.event.get() # obsługa ekranu
        os.system("pause") # pausa w konsoli cmd
        break

# nonzad_125()
    

def zad_78_126():
    import pygame
    import os

    okno = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Primitywy IV")


    # Ciało
    pygame.draw.circle(okno,[255,255,255], [400,50], 40)    # głowa
    pygame.draw.circle(okno,[255,255,255], [400,150], 85)   # tłowie
    pygame.draw.circle(okno,[255,255,255], [400, 400], 200)  # XD nogi?

    pygame.draw.polygon(okno, [200,50,0], [[420,30],[420,70],[550,50]]) # nos

    # Guziki
    pygame.draw.circle(okno,[0,0,0],[400,90], 15)
    pygame.draw.circle(okno,[0,0,0],[400,190], 15)
    pygame.draw.circle(okno,[0,0,0],[400,290], 15)
    pygame.draw.circle(okno,[0,0,0],[400,390], 15)
    pygame.draw.circle(okno,[0,0,0],[400,490], 15)

    # oko # dodatkowo
    pygame.draw.circle(okno,[0,0,0], [380,40], 15)
    pygame.draw.circle(okno,[255,255,255], [380,35], 10)


    pygame.display.update()
    while True:
        pygame.event.get() # obsługa ekranu
        os.system("pause") # pausa w konsoli cmd
        break
# zad_78_126()
    

def zad_79_126():
    import pygame
    import os
    import random

    okno = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Primitywy V")

    # Okienka
    x = random.randint(1,255)
    y = random.randint(1,255)
    z = random.randint(1,255)
        # 1 okno
    pygame.draw.rect(okno, [x,y,z], pygame.Rect(0,0,400,300))
    x = random.randint(1,255)
    y = random.randint(1,255)
    z = random.randint(1,255)
        # 2 okno
    pygame.draw.rect(okno, [x,y,z], pygame.Rect(400,0,800,300))   
    x = random.randint(1,255)
    y = random.randint(1,255)
    z = random.randint(1,255)
        # 3 okno
    pygame.draw.rect(okno, [x,y,z], pygame.Rect(0,300,400,600))   
    x = random.randint(1,255)
    y = random.randint(1,255)
    z = random.randint(1,255)
        # 4 okno
    pygame.draw.rect(okno, [x,y,z], pygame.Rect(400,300,800,600))  
    x = random.randint(1,255)
    y = random.randint(1,255)
    z = random.randint(1,255) 

    # Aktualizacja okna
    pygame.display.update()
    while True:
        pygame.event.get() # obsługa ekranu
        os.system("pause") # pausa w konsoli cmd
        break
# zad_79_126()
    

def zad_80_127():
    import random
    import pygame
    import os

    okno = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Primitywy VI")

    v = 250 # Ilość pięciokątów

    for i in range(1,v,1):
        # Kolory losowe
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)

        # Losowe położenie wiem da się pętlą ale nie chce mi się już myśleć
        a = random.randint(0,800)
        b1 = random.randint(0,800)
        c = random.randint(0,800)
        d = random.randint(0,800)
        e = random.randint(0,800)       
        f = random.randint(0,800)
        h = random.randint(0,800)
        j = random.randint(0,800)
        k = random.randint(0,800)
        l = random.randint(0,800)

        pygame.draw.polygon(okno,[r,g,b],[[a,b1],[c,d],[e,f],[h,j],[k,l]])

    # Aktualizacja okna
    pygame.display.update()
    while True:
        pygame.event.get() # obsługa ekranu
        os.system("pause") # pausa w konsoli cmd
        break
# zad_80_127()
    
def zad_81_129():
    import pygame
    import os
    import time
    import random 

    color = [0,1,2,3,4,5,6,7,8,9]

    for i in range(1,9,1):
        color[i] = random.randint(0,255)

    x = 200
    y = 200

    x_bok = x / 2
    y_bok = y / 2

    x_bok2 = x / 2
    y_bok2 = y / 2

    x_bok3 = x / 2
    y_bok3 = y / 2


    x_spir = x / 2
    y_spir = y / 2

    pre = 2

    kierunek_x = random.randint(pre * -1 ,pre)
    kierunek_y = random.randint(pre * -1 ,pre)

    kierunek_x2 = random.randint(pre * -1 ,pre)
    kierunek_y2 = random.randint(pre * -1 ,pre)

    kierunek_x3 = random.randint(pre * -1 ,pre)
    kierunek_y3 = random.randint(pre * -1 ,pre)

    x_spir_kierunek = 3
    y_spir_kierunek = 3


    if kierunek_x == 0:
        kierunek_x = kierunek_x + 1
    elif kierunek_y == 0:
        kierunek_y = kierunek_y + 1

    elif kierunek_y2 == 0:
        kierunek_y2 = kierunek_y2 + 1
    elif kierunek_x2 == 0:
        kierunek_x2 = kierunek_x2 + 1

    elif kierunek_y3 == 0:
        kierunek_y3 = kierunek_y3 + 1
    elif kierunek_x3 == 0:
        kierunek_x3 = kierunek_x3 + 1
 

    r = 30 

    okno = pygame.display.set_mode([x,y])
    pygame.display.set_caption("Primitywy VII")

    pygame.draw.circle(okno,[255,255,255], [400,300],r)
    pygame.draw.circle(okno,[255,0,255], [x_bok2, y_bok2],30)

    
    for i in range(1,999999,1):
        okno.fill([0,0,0])


    # Ruch kul
        x_bok = x_bok + kierunek_x
        y_bok = y_bok + kierunek_y



        if x_bok <= 0 + r or x_bok >= x - r:
            kierunek_x = kierunek_x * -1
            kierunek_y = random.randint(pre * -1 ,pre)

        elif y_bok <= 0 + r or y_bok >= y - r :
            kierunek_y = kierunek_y * -1
            kierunek_x = random.randint(pre * -1 ,pre)



        x_bok2 = x_bok2 + kierunek_x2
        y_bok2 = y_bok2 + kierunek_y2



        if y_bok2 <= 0 + r or y_bok2 >= y - r :
            kierunek_y2 = kierunek_y2 * -1
            kierunek_x2 = random.randint(pre * -1 ,pre) / 2

        elif x_bok2 <= 0 + r or x_bok2 >= x - r :
            kierunek_y2 = kierunek_y2 * -1
            kierunek_x2 = random.randint(pre * -1 ,pre)  / 2 


    
        x_bok3 = x_bok3 + kierunek_x3
        y_bok3 = y_bok3 + kierunek_y3


        if y_bok3 <= 0 + r or y_bok3 >= y - r :
            kierunek_y3 = kierunek_y3 * -1
            kierunek_x3 = random.randint(pre * -1,pre) / 2

        elif x_bok3 <= 0 + r or x_bok3 >= x - r :
            kierunek_y3 = kierunek_y3 * -1
            kierunek_x3 = random.randint(pre * -1,pre) / 2


        
        # Ruch spiralny 
        # if x_spir_kierunek >= -3:
        #     x_spir_kierunek = x_spir_kierunek - 1
        # elif x_spir_kierunek <= 3:
        #     x_spir_kierunek = x_spir_kierunek + 1
        
        # if y_spir_kierunek >= -3:
        #     y_spir_kierunek = y_spir_kierunek - 1
        # elif y_spir_kierunek <= 3:
        #     y_spir_kierunek = y_spir_kierunek + 1

        


        time.sleep(0.005)
        pygame.draw.circle(okno,[color[3],color[8],color[4]], [x_spir, y_spir],r) # Spiralny 
        pygame.draw.circle(okno,[color[1],color[2],color[3]], [x_bok2, y_bok2],30)
        pygame.draw.circle(okno,[color[4],color[5],color[6]], [x_bok, y_bok],30)
        pygame.draw.circle(okno,[color[7],color[8],color[9]], [x_bok3, y_bok3],30)
        pygame.display.update()

    # Aktualizacja okna
    pygame.display.update()
    while True:
        pygame.event.get() # obsługa ekranu
        os.system("pause") # pausa w konsoli cmd
        break

# zad_81_129()
    

def non_zad_131():
    # pygame.image
    import pygame
    import os
    okno = pygame.display.set_mode([1440,900])
    pygame.display.set_caption("Obrazki")
    obrazek = pygame.image.load("BruceLee.jpg")
    okno.blit(obrazek, [0,0])
    pygame.display.flip()



    while True:
        pygame.event.get() # obsługa ekranu
        os.system("pause") # pausa w konsoli cmd
        break

# non_zad_131()
    
def zad82_132():
    # 5 sekund 5 obrazków
    import pygame
    import random
    # import os
    import time

    okno = pygame.display.set_mode([1920,1080])
    pygame.display.set_caption("Obrazki part 2")

    obrazek = [1,2,3,4,5]

    obrazek[0] = pygame.image.load("BruceLee.jpg")
    obrazek[1] = pygame.image.load("1.jpg")
    obrazek[2] = pygame.image.load("2.jpg")
    obrazek[3] = pygame.image.load("3.jpg")
    obrazek[4] = pygame.image.load("4.jpg")

    for i in range(1,5,1):
        okno.blit(obrazek[random.randint(0,4)], [0,0])
        pygame.display.flip()
        time.sleep(5)
# zad82_132()
        
def  zad_83_132():
    import pygame
    import random
    import os
    import time

    # Rozdzielczość
    y_okno = 300
    x_okno = 240
    okno = pygame.display.set_mode([x_okno,y_okno])
    pygame.display.set_caption("DVD IGOR VERSION")
    vdv = pygame.image.load("DVD_IGOR.jpg")
    vx = 1
    vy = 1
    x = 35
    y = 30
    while True:
        x += vx
        y += vy
        if x < 1:
            vx = 1
        elif x > x_okno - x:
            vx = -1
        if y < 1:
            vy = 1
        elif y > y_okno - y:
            vy = -1 
        okno.fill([255,255,255])
        okno.blit(vdv, [x,y])
        pygame.display.flip()
        time.sleep(0.03)
# zad_83_132()
        
def non_zad_133():              # Nie działa
    import pygame
    import os


    # Rozdzielczość
    y_okno = 400
    x_okno = 300
    okno = pygame.display.set_mode([x_okno,y_okno])
    pygame.display.set_caption("Teskt")
    pygame.font.init()
    czcionka = pygame.font.SysFont("Comic Sans MS", 30)
    napis = czcionka.render("Hello World", False,[0,0,0])
    okno.blit(napis,[0,0])
    pygame.display.flip()
    os.system("pause")

non_zad_133()