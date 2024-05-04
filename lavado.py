class Lavado:
    def __init__(self, id) -> None:
        self.id = id
        self.tiempo = 0
        self.prendas = []

    def agregar_prenda(self, prenda) -> None:
        self.prendas.append(prenda)
        self.actualizar_tiempo()

    def actualizar_tiempo(self) -> None:
        self.tiempo = max(prenda.tiempo_lavado for prenda in self.prendas)
