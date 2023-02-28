import math
import datetime
import pytz

# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu

# Ex 1

def suma(a,b):
    return a+b

print(suma(1,2))

# Ex 2

def paritate():
    a = int(input("Nr: "))
    if a % 2 == 0:
        return True
    else:
        return False

print(paritate())

# Ex 3

def char():
    nume = input("Nume: ")
    prenume1 = input("Prenume 1: ")
    prenume2 = input("Prenume 2: ")

    return len(nume+prenume1+prenume2)

print(char())

# Ex 4

def arie(a,b):
    return a*b

print(arie(2,3))

# Ex 5

def cerc(a):
    return math.pi * a * a

print(cerc(3))

# Ex 6

def find(ch,str):
    if ch in str:
        return True
    else:
        return False
    
print(find(input("Char: "), "Maria"))

# Ex 7

def check_chr(a):
    low = 0
    high = 0

    for i in a:
        if i == i.upper():
            high += 1
        else:
            low += 1
    
    print(f"Numărul de caractere lower case este {low}")
    print(f"Numărul de caractere upper case este {high}")

check_chr(input("String: "))

# Ex 8

def lists(a):
    poz = []

    for i in a:
        if int(i) > 0:
            poz.append(int(i))

    return poz

# print(lists(input("Nr: ").split(" ")))
print(lists([1,2,-5, 0, -70, 90]))

# Ex 9

def compare(a,b):
    if a > b:
        print(f"Primul număr {a} este mai mare decat al doilea număr {b}")
    elif a < b:
        print(f"Al doilea număr {b} este mai mare decat primul număr {a}")
    else:
        print("Numerele sunt egale")

compare(3,4)

# Ex 10 # ???

def sets(nr,set):
    if nr in set:
        set.add(nr)
        print("nu am adaugat numărul în set. Acesta există deja")
        return False
    else:
        set.add(nr)
        print("am adaugat numărul nou în set")
        return True
    
print(sets(2, {2,4,5}))

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google

# Ex 1

def zile_luna(a):
    ian = 31
    feb = 28
    mar = 31
    apr = 30
    mai = 31
    iun = 30
    iul = 31
    aug = 31
    sep = 30
    oct = 31
    noi = 30
    dec = 31

    if a == "ian":
        return ian
    elif a == "feb":
        return feb
    elif a == "mar":
        return mar
    elif a == "apr":
        return apr
    elif a == "mai":
        return mai
    elif a == "iun":
        return iun
    elif a == "iul":
        return iul
    elif a == "aug":
        return aug
    elif a == "sep":
        return sep
    elif a == "oct":
        return oct
    elif a == "noi":
        return noi
    elif a == "dec":
        return dec
    
print(zile_luna("mar"))

# Ex 2

def ops(a,b):
    summ = a + b
    dif = a - b
    prod = a * b
    div = a / b

    return summ, dif, prod, div

x,y,z,u = ops(3,4)

print(f"Suma: {x}")
print(f"Diferenta: {y}")
print(f"Inmultirea: {z}")
print(f"Impartirea: {u}")

# Ex 3

def frequency(a):
    dct = {}

    for i in a:
        dct[i] = a.count(i)

    return dct

print(frequency([0,0,1,2,4,4,4,5,0]))

# Ex 4

def maxim(a,b,c):
    return max(a,b,c)

print(maxim(1,2,3))

# Ex 5

def summ_all(a):
    s = 0

    for i in range(a+1):
        s += i

    return s

print(summ_all(5))

# Exerciții Opționale - Bonus

# Ex 1

def intersect(a,b):
    return set(a) & set(b)

print(intersect([1,1,2,2,3], [2,3,3,4,5,]))

# Ex 2

def reduct(a, red):
    if 0 < red < 100:
        final = a - red / 100 * a
        return int(final)
    else:
        final = f"Invalid discount"
        return final

print(reduct(1000,15))

# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex 1

def time_ro():
    d0 = datetime.datetime.now()
    return f"{d0.strftime('%d')}-{d0.strftime('%m')}-{d0.strftime('%Y')} -> {d0.strftime('%X')}"

print(f"Ora in Romania: {time_ro()}")

def time_china():
    d0 = datetime.datetime.now()
    new_timezone = pytz.timezone("Asia/Shanghai")
    return f"China current time: {datetime.datetime.now(new_timezone)}"
    # return f"{new_timezone.strftime('%d')}-{new_timezone.strftime('%m')}-{new_timezone.strftime('%Y')} -> {new_timezone.strftime('%X')}"

print(time_china())

# Ex 2

def christmas():
    # d0 = datetime.datetime(2023, 2, 9)
    d0 = datetime.datetime.now()
    d1 = datetime.datetime(2023, 12, 25)
    return (d1-d0).days

print(f"Days from now until Chritsmas -> {christmas()}")



# print(pytz.all_timezones)