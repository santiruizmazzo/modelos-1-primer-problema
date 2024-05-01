class Lavanderia:
    def armar_lavados(prendas: list) -> dict:
        prendas.sort(key=lambda prenda: prenda.tiempo_de_lavado)
        lavados = [[] for _ in range(len(prendas))]

        while prendas:
            prenda = prendas.pop()

            i = 0
            mejor_lavado = 0
            tiempo_lavado_max = 0

            while i < len(lavados):
                lavado = lavados[i]
                tiempo_lavado_actual = sum(prenda.tiempo_de_lavado for prenda in lavado)

                if (
                    prenda.puede_estar_en(lavado)
                    and tiempo_lavado_actual >= tiempo_lavado_max
                ):
                    tiempo_lavado_max = tiempo_lavado_actual
                    mejor_lavado = i

                i += 1

            lavados[mejor_lavado].append(prenda)

        lavados = filter(lambda lavado: lavado, lavados)
        return dict(enumerate(lavados, 1))
