# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:


# Ex1

# O variabila este un tip de data care are o locatie in memorie

# Ex2

a = "mike" # string
b = 20 # int
c = 70.223 # float
d = True # bool

# Ex3

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Ex4

c = round(c, 2)
print(type(c))

# Ex5

print(f"Acesta este {a}")
print(f"El are {b} ani")
print(f"El cantareste {c} kg")
print(f"Afara este frig - {d}")

# Ex6

nume = "Andrei"
prenume = "Beril"

print(f"Numele complet are {len(nume+prenume)} caractere")

# Ex7

# lungimea = input("Lungime: ")
# latime = input("Latime: ")
# print(f"Aria dreptunghiului este {int(lungimea) * int(latime)}.")

# Ex8

stringul = "Coral is either the stupidest animal or the smartest rock"
print(f"Stringul 'the' apare de {stringul.count('the')} ori")

# Ex9
stringul = stringul.replace("the", "THE")
print(stringul)

# Ex10

# assert stringul == int
# assert stringul.isdigit()



# Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
# nevoie de Google).

# Ex 1

impar = "abcdefg"
print(f"{impar[int((len(impar)-1) / 2)]}")
print(f"{impar[(len(impar)-1) // 2]}")

# Ex2

# ala1 = "alabala portocala"
# cuv1, cuv2 = ala1.split(" ")
cuv1, cuv2 = input("Words: ").split(" ")
print(cuv1)
print(cuv2)

# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex1

ala2 = "alabala portocala"
ala2_prim = ala2[0]
ala2_ult = ala2[-1]
ala2_UP = ala2_prim.upper()
ala2 = ala2[1:-1]
ala2 = ala2.replace(ala2_prim, ala2_UP)
ala2 = f"{ala2_prim}{ala2}{ala2_ult}"
print(ala2)

# Ex2

user = input("User: ")
passw = input("Pass: ")
secret_pass = len(passw) * "*"

print(f"Parola pt user {user} este {secret_pass} și are {len(passw)} caractere")