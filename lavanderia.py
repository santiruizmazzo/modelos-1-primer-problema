from lavado import Lavado


class Lavanderia:
    def armar_lavados(prendas: list) -> list[Lavado]:
        prendas.sort(key=lambda prenda: prenda.tiempo_lavado)
        lavados = [Lavado(id_lavado) for id_lavado in range(1, len(prendas) + 1)]

        while prendas:
            prenda = prendas.pop()

            i = 0
            mejor_lavado = 0
            tiempo_lavado_max = 0

            while i < len(lavados):
                lavado = lavados[i]

                if prenda.puede_estar_en(lavado) and lavado.tiempo >= tiempo_lavado_max:
                    tiempo_lavado_max = lavado.tiempo
                    mejor_lavado = i

                i += 1

            lavados[mejor_lavado].agregar_prenda(prenda)

        return list(filter(lambda lavado: lavado.tiene_prendas(), lavados))
