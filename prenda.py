class Prenda:
    def __init__(self, id):
        self.id = id
        self.tiempo_lavado = 0
        self.incompatibilidades = []

    def agregar_prenda_incompatible(self, numero_de_prenda):
        self.incompatibilidades.append(numero_de_prenda)

    def tarda_en_lavarse(self, tiempo_lavado):
        self.tiempo_lavado = tiempo_lavado

    def puede_estar_en(self, lavado):
        return set(self.incompatibilidades).isdisjoint(
            map(lambda prenda: prenda.id, lavado.prendas)
        )
