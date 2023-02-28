from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14
    @abstractmethod
    def aria():
        pass

    @abstractmethod
    def descrie():
        print("Cel mai probabil am colturi")


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        print("Setting as property")
        return self.__latura
    
    @latura.getter
    def latura(self):
        print("Get new value")
        return self.__latura

    @latura.setter
    def latura(self, value):
        print("Set new value")
        self.__latura = value

    @latura.deleter
    def latura(self):
        print("Deleting value")
        self.__latura = None

    def aria(self):
        return self.__latura * self.__latura
    
    def descrie(self):
        print("Cel mai probabil am colturi")


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        print("Setting as property")
        return self.__raza
    
    @raza.getter
    def raza(self):
        print("Get new value")
        return self.__raza

    @raza.setter
    def raza(self, value):
        print("Set new value")
        self.__raza = value

    @raza.deleter
    def raza(self):
        print("Deleting value")
        self.__raza = None

    def aria(self):
        return self.PI * self.__raza * self.__raza
    
    def descrie(self):
        print("Eu nu am colturi")


pat = Patrat(5)
print(f"Aria patratului este: {pat.aria()}")
del pat.latura
if pat.latura == None:
    print(f"Latura patratului este: 0")
pat.latura = 3
print(f"Aria patratului este: {pat.aria()}")
pat.descrie()

print()

cerc1 = Cerc(4)
print(f"Aria cercului este: {cerc1.aria()}")
del cerc1.raza
if cerc1.raza == None:
    print("Aria cercului este 0")
cerc1.raza = 5
print(f"Aria cercului este: {cerc1.aria()}")
cerc1.descrie()