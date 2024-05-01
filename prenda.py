class Prenda:
    def __init__(self, id):
        self.id = id
        self.tiempo_de_lavado = 0
        self.incompatibilidades = []

    def es_incompatible_con(self, numero_de_prenda):
        self.incompatibilidades.append(numero_de_prenda)

    def tarda_en_lavarse(self, tiempo_de_lavado):
        self.tiempo_de_lavado = tiempo_de_lavado
