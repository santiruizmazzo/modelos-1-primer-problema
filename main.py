import sys
from prenda import Prenda


class TipoDeLinea:
    COMENTARIO = "c"
    PROBLEMA = "p"
    INCOMPATIBILIDAD = "e"
    TIEMPO_LAVADO = "n"


PATH_CARPETA_PROBLEMAS = "problemas/"
SUFIJO_ARCHIVO_PROBLEMA = "_problema.txt"
ARCHIVO_SOLUCION = "solucion.txt"
MODO_ESCRITURA = "w"


def cantidad_de_prendas_segun(archivo) -> int:
    linea = archivo.readline().split()

    while linea[0] != TipoDeLinea.PROBLEMA:
        linea = archivo.readline().split()

    return int(linea[2])


def cargar_prendas_desde(path_problema) -> dict:

    with open(path_problema) as archivo:
        cantidad_prendas = cantidad_de_prendas_segun(archivo)
        prendas = [Prenda(id_prenda) for id_prenda in range(1, cantidad_prendas + 1)]

        for linea in archivo:
            palabras = linea.split()
            tipo = palabras[0]
            id_prenda = int(palabras[1])
            prenda_actual = prendas[id_prenda - 1]

            match tipo:
                case TipoDeLinea.INCOMPATIBILIDAD:
                    id_prenda_incompatible = int(palabras[2])
                    prenda_actual.es_incompatible_con(id_prenda_incompatible)
                case TipoDeLinea.TIEMPO_LAVADO:
                    tiempo_lavado = int(palabras[2])
                    prenda_actual.tarda_en_lavarse(tiempo_lavado)

    return prendas


def ordenar_prendas_por_tiempo(prendas) -> list:
    return list(sorted(prendas, key=lambda prenda: prenda.tiempo_de_lavado))


def armar_lavados_para(prendas) -> dict:
    prendas_ordenadas = ordenar_prendas_por_tiempo(prendas)
    lavados = [[] for _ in range(len(prendas_ordenadas))]

    while prendas_ordenadas:
        prenda_actual = prendas_ordenadas.pop()

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


def escribir_solucion_segun(lavados):
    with open(ARCHIVO_SOLUCION, MODO_ESCRITURA) as archivo:
        for numero_lavado, lavado in lavados.items():
            for prenda in lavado:
                archivo.write(f"{prenda.id} {numero_lavado}\n")


def mostrar_tiempos_de_lavado(lavados):
    lavados = dict(
        enumerate(
            start=1,
            iterable=map(
                lambda lavado: max(prenda.tiempo_de_lavado for prenda in lavado),
                lavados.values(),
            ),
        )
    )
    for numero, tiempo in lavados.items():
        print(f"Lavado {numero} -> Tiempo: {tiempo}")
    print(f"Tiempo total de lavado: {sum(lavados.values())}")


def path_archivo_problema_desde_input() -> str:
    nombre_archivo = sys.argv[1]
    return PATH_CARPETA_PROBLEMAS + nombre_archivo + SUFIJO_ARCHIVO_PROBLEMA


if __name__ == "__main__":
    path_problema = path_archivo_problema_desde_input()
    prendas = cargar_prendas_desde(path_problema)
    lavados = armar_lavados_para(prendas)
    escribir_solucion_segun(lavados)
    mostrar_tiempos_de_lavado(lavados)
