from lavado import Lavado
from prenda import Prenda


class Lavanderia:
    def armar_lavados(prendas: list[Prenda]) -> list[Lavado]:
        prendas.sort(key=lambda prenda: prenda.tiempo_lavado)
        lavados = []

        while prendas:
            prenda = prendas.pop()

            i = 0
            i_mejor_lavado = -1
            tiempo_lavado_max = -1

            while i < len(lavados):
                lavado = lavados[i]

                if prenda.puede_estar_en(lavado) and lavado.tiempo >= tiempo_lavado_max:
                    tiempo_lavado_max = lavado.tiempo
                    i_mejor_lavado = i

                i += 1

            if i_mejor_lavado < 0:
                nuevo_lavado = Lavado(len(lavados) + 1)
                nuevo_lavado.agregar_prenda(prenda)
                lavados.append(nuevo_lavado)
            else:
                lavados[i_mejor_lavado].agregar_prenda(prenda)

        return lavados
