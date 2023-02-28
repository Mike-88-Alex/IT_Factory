import random

# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu

# Ex 1

# Daca if este True se executa si nu se mai trece la else, iar daca if se avalueaza ca False atunci se executa else

# Ex 2

# varianta 1 - citire direct int

# x = int(input("Nr: "))

# if type(x) == int:
#     print(f"{x} este nr natural")


# varianta 2 - citire string

x = input("Nr: ")

# probabil asta se cerea din enuntul problemei ? Dar funcioneaza doar daca citim un string care poate fi potential int

if x.isdigit():
    print(f"{x} este nr natural")


# Ex 3

x = 2

if x > 0:
    print(f"{x} > 0 - pozitiv")
elif x < 0:
    print(f"{x} < 0 - negativ")
else:
    print(f"{x} este neutru")

# Ex 4

x = -3

if x >= -2 and x <= 13:
# if -2 <= x <= 13:
    print(f"{x} este intre -2 si 13")
else:
    print(f"{x} nu este intre -2 si 13")

# Ex 5

x = 6
y = 3

if (x-y) < 5:
    print("Diferenta 'x-y' este mai mica decat 5")
else:
    print("Diferenta 'x-y' nu este mai mica decat 5") # merge si fara else

# ex 6

x = 4

if not (x >= 5) or not (x <= 27):
# if not (5 <= x <= 27):
    print(f"x < 5 sau x > 27")
else:
    print(f"x este intre 5 si 27")

# Ex 7

x = 3
y = 4

if x == y:
    print("x si y sunt egale")
elif x > y:
    print(f"x({x}) este mai mare")
else:
    print(f"y({y}) este mai mare")

# Ex 8

x = 2 # se dau valori oarecare x / y / z
y = 3
z = 2

if x == y or x == z or y == z:
    print("Triunghi isoscel")
elif x == y and y == z:
    print("Triunghi echilateral")
else:
    print("Triunghi oarecare")

# Ex 9

a = input("O singura litera: ").lower()

# if a == "a" or a == "e" or a == "i" or a == "o" or a == "u": # var 1
if a in "aeiou": # var 2 cu in keyword
    print("Litera este vocala")
else:
    print("Litera este consoana")

# Ex 10

a = 8 # sau il citesc de la tast cu int(input("Nr "))

if a > 9:
    print("A")
elif a > 8:
    print("B")
elif a > 7:
    print("C")
elif a > 6:
    print("D")
elif a > 4:
    print("E")
else:
    print("F")


# Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google

# Ex 1

x = 123

if len(str(x)) >= 4:
    print(f"{x} are min 4 cifre / digits")
else:
    print(f"{x} nu are min 4 cifre / digits")

# Ex 2

x = 1212121

if len(str(x)) == 6:
    print(f"{x} are exact 6 cifre / digits")
elif len(str(x)) > 6:
    print(f"{x} are mai mult de 6 cifre / digits") # merge si doar cu if
else:
    print(f"{x} are mai putin de 6 cifre / digits")

# Ex 3

x = 2

if x % 2 == 0:
    print(f"{x} este par")
else:
    print(f"{x} este impar")

# Ex 4

x, y, z = 2, 3, 1

if x > y and x > z:
    print(f"x({x}) este cel mai mare")
elif y > x and y > z:
    print(f"y({y}) este cel mai mare")
else:
    print(f"z({z}) este cel mai mare")

# Ex 5

x, y, z = 31, 90, 60

if (x + y + z) == 180:
    print("Laturile compun un triunghi")
else:
    print("Laturile nu compun un triunghi")

# Ex 6

word = "Coral is either the stupidest animal or the smartest rock"

x = int(input("Nr: "))
# print(f"{word[:-x]}") # nu stiu cum as incorpora o struct if aici

if x: # probabil asa ?!
    print(f"{word[:-x]}")

# Ex 7

word_new = f"{word[:5]}{word[-5:]}" # nu stiu cum as incorpora o struct if aici
# print(word_new)

if word_new: # probabil asa ?!
    print(word_new)

# Ex 8

rock = word.find("rock") # nu stiu cum as incorpora o struct if aici

if rock: # probabil asa ?!
    print(f"{word[:rock]}1") # doar ca imi tipareste cu inca 1 spatiu dupa smartest
    # ca sa-mi afiseze "Coral is either the stupidest animal or the smartest" fara spatiu trebuie -> word[:rock-1] <- ca algoritm in loc


# Exerciții Bonus (may need google)

# Ex 11

dice_roll = random.randint(1, 6)
guess = int(input("Nr ghicit (1-6): "))

if guess < dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}.")
elif guess > dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}.")
else:
    print(f"Ai ghicit. Felicitări! Ai ales {guess} si zarul a fost {dice_roll}.")


# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex 1

word1 = input("String: ")
assert word1[0].lower() == word1[-1].lower(), "Nu sunt la fel"

# Ex 2

word2 = "0123456789"
sequence = input("Par / impar: ").lower()

if sequence == "par":
    print(word2[::2])
else:
    print(word2[1::2])

