import sys


class TipoDeLinea:
    COMENTARIO = "c"
    PROBLEMA = "p"
    INCOMPATIBILIDAD = "e"
    TIEMPO_LAVADO = "n"


PATH_CARPETA_PROBLEMAS = "problemas/"
SUFIJO_ARCHIVO_PROBLEMA = "_problema.txt"
ARCHIVO_SOLUCION = "solucion.txt"
MODO_ESCRITURA = "w"


def cargar_cantidad_de_prendas(archivo) -> int:
    linea = archivo.readline().split()

    while linea[0] != TipoDeLinea.PROBLEMA:
        linea = archivo.readline().split()

    return int(linea[2])


def cargar_incompatibilidad(palabras, prendas):
    numero_prenda = int(palabras[1])
    numero_prenda_incompatible = int(palabras[2])
    prendas[numero_prenda]["incompatible_con"].append(numero_prenda_incompatible)


def cargar_tiempo_de_lavado(palabras, prendas):
    numero_prenda = int(palabras[1])
    tiempo_lavado = int(palabras[2])
    prendas[numero_prenda]["tiempo_lavado"] = tiempo_lavado


def cargar_prendas_desde(path_problema) -> dict:

    with open(path_problema) as archivo:
        cantidad_prendas = cargar_cantidad_de_prendas(archivo)
        prendas = {
            numero_prenda: {"tiempo_lavado": 0, "incompatible_con": []}
            for numero_prenda in range(1, cantidad_prendas + 1)
        }

        for linea in archivo:
            palabras = linea.split()
            tipo = palabras[0]

            match tipo:
                case TipoDeLinea.INCOMPATIBILIDAD:
                    cargar_incompatibilidad(palabras, prendas)
                case TipoDeLinea.TIEMPO_LAVADO:
                    cargar_tiempo_de_lavado(palabras, prendas)

    return prendas


def ordenar_prendas_por_tiempo(prendas) -> list:
    return list(
        map(
            lambda item: (item[0], item[1]["tiempo_lavado"]),
            sorted(
                prendas.items(),
                key=lambda prenda: prenda[1]["tiempo_lavado"],
            ),
        )
    )


def armar_lavados(prendas) -> dict:
    prendas_ordenadas = ordenar_prendas_por_tiempo(prendas)
    lavados = [[] for _ in range(len(prendas_ordenadas))]

    while prendas_ordenadas:
        prenda_actual = prendas_ordenadas.pop()

        i = 0
        mejor_lavado = 1
        mayor_tiempo_de_lavado = 0

        while i < len(lavados):
            lavado_actual = lavados[i]
            prendas_incompatibles = set(prendas[prenda_actual[0]]["incompatible_con"])
            tiempo_lavado_actual = sum(n for _, n in lavado_actual)

            if prendas_incompatibles.isdisjoint(
                map(lambda prenda: prenda[0], lavado_actual)
            ):

                if tiempo_lavado_actual >= mayor_tiempo_de_lavado:
                    mayor_tiempo_de_lavado = tiempo_lavado_actual
                    mejor_lavado = i

            i += 1

        lavados[mejor_lavado].append(prenda_actual)

    lavados = filter(lambda lavado: lavado, lavados)
    return dict(enumerate(lavados, 1))


def escribir_solucion(lavados):
    with open(ARCHIVO_SOLUCION, MODO_ESCRITURA) as archivo:
        for numero_lavado, lavado in lavados.items():
            for prenda in lavado:
                archivo.write(f"{prenda[0]} {numero_lavado}\n")


def mostrar_tiempos_de_lavado(lavados):
    lavados = dict(
        enumerate(
            start=1,
            iterable=map(
                lambda lavado: max(
                    tiempo_lavado for numero_prenda, tiempo_lavado in lavado
                ),
                lavados.values(),
            ),
        )
    )
    for numero, tiempo in lavados.items():
        print(f"Lavado {numero} -> Tiempo: {tiempo}")
    print(f"Tiempo total de lavado: {sum(lavados.values())}")


def crear_path_problema_desde_input() -> str:
    prefijo_archivo = sys.argv[1]
    return PATH_CARPETA_PROBLEMAS + prefijo_archivo + SUFIJO_ARCHIVO_PROBLEMA


if __name__ == "__main__":
    path_problema = crear_path_problema_desde_input()
    prendas = cargar_prendas_desde(path_problema)
    lavados = armar_lavados(prendas)
    escribir_solucion(lavados)
    mostrar_tiempos_de_lavado(lavados)
