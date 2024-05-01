class Lavanderia:
    def armar_lavados(prendas: list) -> dict:
        prendas.sort(key=lambda prenda: prenda.tiempo_de_lavado)
        lavados = [[] for _ in range(len(prendas))]

        while prendas:
            prenda_actual = prendas.pop()

            i = 0
            mejor_lavado = 1
            mayor_tiempo_de_lavado = 0

            while i < len(lavados):
                lavado_actual = lavados[i]
                prendas_incompatibles = set(prenda_actual.incompatibilidades)
                tiempo_lavado_actual = sum(
                    prenda.tiempo_de_lavado for prenda in lavado_actual
                )

                if prendas_incompatibles.isdisjoint(
                    map(lambda prenda: prenda.id, lavado_actual)
                ):

                    if tiempo_lavado_actual >= mayor_tiempo_de_lavado:
                        mayor_tiempo_de_lavado = tiempo_lavado_actual
                        mejor_lavado = i

                i += 1

            lavados[mejor_lavado].append(prenda_actual)

        lavados = filter(lambda lavado: lavado, lavados)
        return dict(enumerate(lavados, 1))
