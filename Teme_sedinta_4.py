import random

# Exerciții obligatorii - grad de dificultate: Usor spre Mediu

# Ex 1

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
    print(f"Masina mea preferata este {masini[i]}")

print(40 * "*")

for i in masini:
    print(f"Masina mea preferata este {i}")

print(40 * "*")

c = 0

while c < len(masini):
    print(f"Masina mea preferata este {masini[c]}")
    c += 1

print(40 * "*")

# Ex 2

for i in range(len(masini)):
    # if i == 0 or i == len(masini)-1:
    if masini[i] in ["Audi", "Opel"]:
        continue
    else:
        masini[i] = masini[i].upper()
else:
    print(masini)

# for i, masina in enumerate(masini):
#     if masina in ["Audi", "Opel"]:
#         continue
#     else:
#         masini[i] = masini[i].upper()
# else:
#     print(masini)

# for i in range(1,len(masini)-1):
#     masini[i] = masini[i].upper()
# else:
#     print(masini)

print(40 * "*")

# Ex 3

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for i in masini:
    if i != "Mercedes":
        print(f"Am găsit mașina {i}. Mai căutam")
    elif i == "Mercedes":
        print("am găsit mașina dorită de dvs")
        break

print(40 * "*")

# Ex 4

for i in masini:
    if i == "Trabant" or i == "Lăstun":
        continue
    print(f"S-ar putea să vă placă mașina {i}.")

print(40 * "*")

# Ex 5

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in masini:
    if i == "Trabant" or i == "Lăstun":
        masini_vechi.append(i)
        # i = "Tesla"
        # i = i.replace(i,"Tesla")

# for i in range(len(masini)):
#     if masini[i] == "Trabant" or masini[i] == "Lăstun":
#         masini[i] = "Tesla"

# for i, k in enumerate(range(len(masini))):
for i, k in enumerate(masini):
    # if masini[i] == "Trabant" or masini[i] == "Lăstun":
    if k in ["Trabant", "Lăstun"]:
        masini[i] = "Tesla"

for i in masini:
    if i == "Tesla":
        print(f"Modelele noi: {i}")

print(40 * "*")

for i in masini_vechi:
    print(f"Modelele vechi: {i}")

print(40 * "*")

# Ex 6

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

print("Masini sub 15000 euro")
print()
for k, v in pret_masini.items():
    if v <= 15000:
        print(k)

print(40 * "*")

for k, v in pret_masini.items():
    if v <= 15000:
        print(f"{k} - {v}e")

print(40 * "*")

for k, v in pret_masini.items():
    if v <= 15000:
        print(f"Pentru un buget de sub 15000 euro puteți alege mașina {k}")

print(40 * "*")

# Ex 7

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
c = 0
for i in numere:
    if i == 3:
        c += 1
print(c)

print(40 * "*")

# Ex 8

s = 0
for i in numere:
    s += i
print(s)

print(40 * "*")

# Ex 9

maxx = 0
for i in numere:
    if i > maxx:
        maxx = i
print(maxx)

print(40 * "*")

# Ex 10

# var 1 - for

for i in range(len(numere)):
    if numere[i] > 0:
        # numere[i] = -numere[i]
        numere[i] *= -1
print(numere)

# var 2 - enumerate

for i, num in enumerate(numere):
    # if numere[i] > 0:
    if num > 0:
        # num *= -1
        numere[i] = num * (-1)
print(numere)

print(40 * "*")

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
# Google.

# Ex 1

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if i > 0:
        numere_pozitive.append(i)
    elif i < 0:
        numere_negative.append(i)

print(f"Nr pare - {numere_pare}") 
print(f"Nr impare - {numere_impare}")
print(f"Nr > 0 - {numere_pozitive}")
print(f"Nr < 0 -{numere_negative}")

print(40 * "*")

# Ex 2

# Am tras cu ochiul putin pe net si am inteles pana la urma metoda de sortrare. Var1 este de pe net si Var2 este varianta modificata si facuta de mine. Flag-ul switch ajuta la eficienta algoritmului in caz ca nu mai sunt elemente de sortat si se asigura ca se iese din primul `for` care si-ar continua treaba indiferent daca ar mai fi sau nu numere de sortat, pt eficienta la runtime.

# var 1

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
a = len(alte_numere)

for i in range(a):
    switch = False
    for j in range(a-i-1):
        if alte_numere[j] > alte_numere[j+1]:
            alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
            switch = True
    if not switch:
        break

print(alte_numere)

# var 2

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
a = len(alte_numere)

for i in range(a):
    switch = False
    for j in range(1, a-i):
        if alte_numere[j] < alte_numere[j-1]:
            alte_numere[j], alte_numere[j-1] = alte_numere[j-1], alte_numere[j]
            switch = True
    if not switch:
        break

print(alte_numere)

print(40 * "*")

# Ex 3

numar_secret = random.randint(1,30)
numar_ghicit = None

while True:
    numar_ghicit = int(input("Alege un nr 1-30: "))
    if numar_ghicit < numar_secret:
        print("Nr secret e mai mare\n")
    elif numar_ghicit > numar_secret:
        print("Nr secret e mai mic\n")
    else:
        print("Felicitări! Ai ghicit!\n")
        break

print(40 * "*")

# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex 1

nr = int(input("Alege un nr: "))

for i in range(1,nr+1):
    print(f"{i}" * i)

print(40 * "*")

# Ex 2

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in tastatura_telefon:
    for j in i:
        print(f"Cifra curentă este {j}")