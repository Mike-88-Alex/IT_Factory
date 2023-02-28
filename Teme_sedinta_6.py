import math
from datetime import date

# Exerciții obligatorii - grad de dificultate: Usor spre Mediu

# Ex 1

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(self.raza)
        print(self.culoare)

    def aria(self):
        return round(math.pi * (self.raza ** 2), 1)

    def diametru(self):
        return self.raza * 2
    
    def circumferinta(self):
        return round(math.pi * 2 * self.raza, 1)
    
cerc1 = Cerc(3, "albastru")
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

# Ex 2

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Acesta este un dreptinghi {self.culoare} cu lungime de {self.lungime} si latime de {self.latime}")

    def aria(self):
        return self.lungime * self.latime
    
    def perimetru(self):
        return (self.lungime + self.latime) * 2
    
    def schimba_culoarea(self, culo):
        self.culoare = culo

drept1 = Dreptunghi(4, 2, "galben")
drept1.descrie()
print(drept1.aria())
print(drept1.perimetru())
drept1.schimba_culoarea("albastru")
drept1.descrie()

# Ex 3

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Angajatul {self.nume} {self.prenume} - salariu -> {self.salariu}")

    def nume_complet(self):
        print(f"{self.nume} {self.prenume}")

    def salariu_lunar(self):
        return self.salariu
        
    def salariu_anual(self):
        return self.salariu * 12
    
    def marire_salariu(self, procent):
        self.salariu += int((procent / 100) * self.salariu)

mike = Angajat("Sandache", "Mihai", 10000)
mike.descrie()
mike.nume_complet()
print(mike.salariu_lunar())
print(mike.salariu_anual())
mike.marire_salariu(50)
print(mike.salariu_lunar())

# Ex 4

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular} are in contul {self.iban} suma de {self.sold} lei")
    
    def debitare_cont(self, suma):
        self.sold -= suma

    def creditare_cont(self,suma):
        self.sold += suma

mihai = Cont("1983128", "Sandache Mihai", 10000)
mihai.afisare_sold()
mihai.debitare_cont(50)
mihai.afisare_sold()
mihai.creditare_cont(100)
mihai.afisare_sold()


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google

# Ex 1

class Factura:
    seria = 5478

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.nr = numar
        self.nume_prod = nume_produs
        self.cant = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cant):
        self.cant = cant

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_prod = nume

    def genereaza_factura(self):
        # print(f"Factura seria {self.seria} numar {self.nr}")
        # print(f"Data: {date.today()}")
        # print(f"{self.nume_prod} | cantitate | pret bucata | Total")
        # print(f"0746 098 769 | {self.cant : ^9} | {self.pret_buc : ^9} | {self.cant * self.pret_buc : >9}")

        print(f"Factura seria {self.seria} numar {self.nr}\n" 
              f"Data: {date.today()}\n" 
              f"{self.nume_prod:^12} | {'cantitate':^12} | {'pret bucata':^12} | {'Total':^12}\n" 
              f"{'0746 098 769':^12} | {self.cant:^12} | {self.pret_buc:^12} | {self.cant * self.pret_buc:^12}")

fact = Factura(1, "Cascaval", 1, 100)
fact.genereaza_factura()
fact.schimba_cantitatea(2)
fact.schimba_pretul(150)
fact.schimba_nume_produs("Miere")
fact.genereaza_factura()

# Ex 2

class Masina:
    marca = "BMW"
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {"Albastru", "Verde", "Negru", "Rosu", "Gri Metalizat", "Galben"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.max = viteza_maxima

    def descrie(self):
        matr = None
        if self.inmatriculata == True:
            matr = "Da"
        else:
            matr = "Nu"
        print(f"Marca {self.marca} - viteza {self.viteza_actuala} - culoare {self.culoare} - inmatriculare - {self.inmatriculata}")

        print(f"Marca {self.marca} - viteza {self.viteza_actuala} - culoare {self.culoare} - inmatriculata - {matr}")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, cul):
        if cul in self.culori_disponibile:
            self.culoare = cul
        else:
            raise "Aceasta culoare nu exista !"
        
    def accelereaza(self, vit):
        if vit < 0:
            raise "Viteza nu poate scade sub 0"
        elif vit > self.max:
            self.viteza_actuala = self.max
        else:
            self.viteza_actuala = vit

    def franeaza(self):
        self.viteza_actuala = 0

bmw = Masina("X5", 350)
bmw.descrie()
bmw.vopseste("Albastru")
bmw.descrie()
bmw.accelereaza(360)
bmw.descrie()
bmw.franeaza()
bmw.descrie()


# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex 1

class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
    
    def finalizeaza_task(self, nume):
        # del self.todo[nume]
        self.todo.pop(nume)

    def afișează_todo_list(self):
        li = []
        # li2 = []

        for k in self.todo.keys():
            li.append(k)
        print(li)
        # for k, v in self.todo.items():
        #     li2.append((k, v))
        # print(li2)
    
    def afișează_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo.values():
            check = input("Vreti sa adaugati acest task in lista personala ? Y / N ").lower()
            if check == "n":
                print("ok, nu adaugam nimic")
            elif check == "y":
                detalii = input("Detalii ? ")
                self.todo[nume_task] = detalii

my_list = TodoList()
my_list.adauga_task("invatat python", "Mihai")
my_list.adauga_task("invatat C#", "Alex")
my_list.adauga_task("Desen tehnic", "Ion")
my_list.finalizeaza_task("Desen tehnic")
my_list.afișează_todo_list()
my_list.afișează_detalii_suplimentare("Desen tehnic")
my_list.afișează_todo_list()