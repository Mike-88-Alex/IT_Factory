# Ex 1

a = ["do", "re", "mi", "fa", "sol", "la", "si"]

print(a)
a = a[::-1]

print(a)
a.reverse()
print(a)

# Ex 2

print(f"do are frecventa -> {a.count('do')}")

# Ex 3

b = [3,1,0,2]
c = [6,5,4]

# Varianta 1

d = b[:]
d.extend(c)
print(d)

# Varianta 2

d = b + c
print(d)

# Ex 4

d.sort()
print(f"lista d - {d}")
d.remove(0)
print(f"lista d fara '0' - {d}")

# Ex 5

# var 1

if len(d) == 0:
    print("Lista d este goala")
else:
    print("Lista nu este goala")

# var 2

if d:
    print("Lista nu este goala")
else:
    print("Lista d este goala")

# Ex 6

d.clear()

# Ex 7

if len(d):
    print("Lista nu este goala")
else:
    print("Lista d este goala")

# Ex 8

dict1 = {"Ana" : 8, "Gigel" : 10, "Dorel" : 5}

# for i in dict1.keys():
#     print(i)
print(list(dict1.keys()))

# Ex 9 - ??

# for i in dict1:
#     print(f"{i} a luat nota {dict1[i]}")
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")

# Ex 10

dict1.update(Dorel = 6)

# for i in dict1:
#     if i == "Dorel":
#         print(dict1[i])
print(f"Dorel - nota {dict1['Dorel']}")

# Ex 11

del dict1["Gigel"]
dict1.update(Ionica = 9)

# for i in dict1:
#     print(i)
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Dorel a luat nota {dict1['Dorel']}")
print(f"Ionica a luat nota {dict1['Ionica']}")

# Ex optionale - var 1

jucatori = ["Mihai", "Bogdan", "Ionut", "Alin", "Mircea"]
schimbari_max = 3
schimbari_efectuate = 0
jucator = "Mihai"

if jucator in jucatori and schimbari_max > 0:
    exit = jucatori.pop(jucatori.index("Mihai"))
    jucatori.append("George")
    enter = jucatori[-1]
    schimbari_max -= 1
    schimbari_efectuate += 1
elif jucator not in jucatori:
    print("nu se poate efectua schimbarea deoarece jucatorul x nu e in teren")

print(f"A intrat {enter} a iesit {exit}, mai sunt {schimbari_max} schimbari")

jucator = "Ion"

if jucator in jucatori and schimbari_max > 0:
    exit = jucatori.pop(jucatori.index("Mihai"))
    jucatori.append("George")
    enter = jucatori[-1]
    schimbari_max -= 1
    schimbari_efectuate += 1
elif jucator not in jucatori:
    print(f"nu se poate efectua schimbarea deoarece jucatorul {jucator} nu e in teren")
    print(f"Mai sunt {schimbari_max} schimbari")


# Ex 1 - Optional - var 2

jucatori = ["Mihai", "Ion", "Gica", "Bogdan", "Alex"]
schimbari_max = 3
schimbari_efectuate = 0

jucator = "Mihai"
jucator_nou = "Aurelian"

if jucator in jucatori and schimbari_max > 0:
    jucatori.remove(jucator)
    exit = jucator
    jucatori.append(jucator_nou)
    schimbari_max -= 1
    schimbari_efectuate += 1
    print(f"A intrat {jucator_nou}, a iesit {exit}, mai ai {schimbari_max} schimbari")
elif jucator not in jucatori:
    print(f"nu se poate efectua schimbarea deoarece jucătorul {jucator} nu e în teren")
    print(f"mai ai {schimbari_max} schimbari")


jucator = "Sebi"
jucator_nou = "Mandu"

if jucator in jucatori and schimbari_max > 0:
    jucatori.remove(jucator)
    exit = jucator
    jucatori.append(jucator_nou)
    schimbari_max -= 1
    schimbari_efectuate += 1
    print(f"A intrat {jucator_nou}, a iesit {exit}, mai ai {schimbari_max} schimbari")
elif jucator not in jucatori:
    print(f"nu se poate efectua schimbarea deoarece jucătorul {jucator} nu e în teren")
    print(f"mai ai {schimbari_max} schimbari")

# Sesiune in echipa

# Ex 1

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add("luni")
print(zile_sapt)

# Ex 2

if weekend.issubset(zile_sapt):
    print("Yes weekend is a subset of zile_sapt")
else:
    print("No weekend is not a subset of zile_sapt")

# Ex 3

print(f"Diferenta dintre 'zile_sapt' si 'weekend' este: {zile_sapt.difference(weekend)}")
print(f"Diferenta dintre 'weekend' si 'zile_sapt' este: {weekend.difference(zile_sapt)}")

# Ex 4

print(f"Intersectia elementelor dintre seturi este: {zile_sapt.intersection(weekend)}")
