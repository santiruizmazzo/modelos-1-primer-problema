import pprint


class TipoDeLinea:
    COMENTARIO = "c"
    PROBLEMA = "p"
    INCOMPATIBILIDAD = "e"
    TIEMPO_LAVADO = "n"


def cargar_parametros_del_problema(archivo):
    linea = archivo.readline().split()

    while linea[0] != TipoDeLinea.PROBLEMA:
        linea = archivo.readline().split()

    return int(linea[2]), int(linea[3])


def cargar_problema_desde_archivo():
    ARCHIVO_PROBLEMA = "primer_problema.txt"

    with open(ARCHIVO_PROBLEMA) as archivo:

        cantidad_prendas, cantidad_incompatibilidades = cargar_parametros_del_problema(
            archivo
        )

        prendas = {
            numero_prenda: {"tiempo_lavado": 0, "incompatible_con": []}
            for numero_prenda in range(1, cantidad_prendas + 1)
        }

        for linea in archivo:
            palabras = linea.split()
            tipo = palabras[0]

            match tipo:
                case TipoDeLinea.INCOMPATIBILIDAD:
                    numero_prenda = int(palabras[1])
                    numero_prenda_incompatible = int(palabras[2])
                    prendas[numero_prenda]["incompatible_con"].append(
                        numero_prenda_incompatible
                    )
                case TipoDeLinea.TIEMPO_LAVADO:
                    numero_prenda = int(palabras[1])
                    tiempo_lavado = int(palabras[2])
                    prendas[numero_prenda]["tiempo_lavado"] = tiempo_lavado

        return prendas


def main() -> None:
    prendas = cargar_problema_desde_archivo()

    prendas_ordenadas = list(
        map(
            lambda item: item[0],
            sorted(
                prendas.items(),
                key=lambda item: item[1]["tiempo_lavado"],
            ),
        )
    )

    lavados = [[] for _ in range(len(prendas_ordenadas))]

    while prendas_ordenadas:
        prenda_actual = prendas_ordenadas.pop()
        asignada_a_lavado = False

        i = 0
        while not asignada_a_lavado and i < len(lavados):
            lavado_actual = lavados[i]

            if set(prendas[prenda_actual]["incompatible_con"]).isdisjoint(
                lavado_actual
            ):
                lavado_actual.append(prenda_actual)
                asignada_a_lavado = True
            i += 1

    lavados = list(
        map(
            lambda lavado: [
                (prenda, prendas[prenda]["tiempo_lavado"]) for prenda in lavado
            ],
            filter(lambda lavado: lavado, lavados),
        )
    )
    pprint.pprint(lavados)
    lavados = list(
        map(
            lambda lavado: max(
                tiempo_lavado for numero_prenda, tiempo_lavado in lavado
            ),
            lavados,
        )
    )
    pprint.pprint(lavados)
    print(sum(lavados))


if __name__ == "__main__":
    main()
