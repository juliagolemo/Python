# Vererbung - Übergabe von Eigenschaften

class Auto():
    def __init__(self, marke, modell, jahr, raeder, tueren, ps):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.raeder = 4
        self.tueren = tueren
        self.ps = ps

    def begruessung(self):
        print("Hallo, ich bin" + self.marke)

    def fahren(self):
        print("Brmrm" * int(self.ps/10))


class Sportwagen(Auto):
    def __init__(self, marke, modell, jahr, raeder, tueren, ps, folierung):
        super().__init__(marke, modell, jahr, raeder, tueren, ps)
        self.folie = folierung
        self.auspuff = 2

    def turbo(self):
        print("Turbo activated")
    def fahren(self):

sw1 = Sportwagen(marke="Seat", modell="Ibiza", jahr=2020, raeder=4, tueren=2, ps=500, folierung="matt")
print(sw1.modell)
print(sw1.turbo)



# Attribute vererben: super().__init__(...)
