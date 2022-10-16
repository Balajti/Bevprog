class Developer:
    def __init__(self, name, job, position):
        self._name = name
        self._job = job
        self._position = position
        print("-- Develper created. --")
        print(f"{self._name} a {self._job}-en dolgozik {self._position} szerepkorben")

    def __eq__(self, other):
        if self._job == other._job:
            print(f"{self._name} and {other._name} are working together")

if __name__ == "__main__":
    d1 = Developer("Ricsi", "Tech", "Frontend")
    d2 = Developer("Angéla", "ZerTeng", "Frontend")
    d3 = Developer("Peti", "kefERP", "Frontend")
    d4 = Developer("Éva", "Tech", "Frontend")
    print()
    print(d4 == d1)






