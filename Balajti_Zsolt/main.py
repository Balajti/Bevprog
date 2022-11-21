class Kutya():
    def __init__(self, name, age, fajta):
        self.name = name
        self._age = age
        self.fajta = fajta
    
    def __set__(self, age):
        self._age = age

    def __get__(self):
        return self._age 

    def __str__(self) :
        return (f"{self.name} egy {self.fajta} fajta kutya aki {self._age * 7} éves")
    
    def __eq__(self, other) :
        return self.name == other.name and self._age == other._age and self.fajta == other.fajta
    
    def ugat(self):
        print(f"{self.name}: VAÚ")
    


if __name__ == "__main__":
    kutyak = []
    k1 = Kutya("Csibész", 9, "vizsla")
    k2 = Kutya("Csibész", 9, "vizsla" )
    k3 = Kutya("Csibész3", 91, "vizsla")
    k4 = Kutya("Csibész4", 92, "nemvizsla")

    kutyak.append(k1)
    kutyak.append(k2)
    kutyak.append(k3)
    kutyak.append(k4)

    fajtak = set()
    fajtakdic = dict()
    counter = 0
    for i in kutyak:
        i.ugat()
        fajtak.add(i.fajta)

    x = 0
    for i in fajtak:
        for l in kutyak:
            if i == l.fajta:
                counter +=1
        fajtakdic[x] = i, counter
        counter = 0
        x += 1

    print(fajtakdic)
