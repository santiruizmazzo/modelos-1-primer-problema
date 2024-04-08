ARCHIVO_PROBLEMA = 'primer_problema.txt'

COMENTARIO = 'c'
PROBLEMA = 'p'
INCOMPATIBILIDAD = 'e'
TIEMPO_LAVADO = 'n'

def main() -> None:
    # incompatibilidades = set([])
    # incompatibilidades.add(frozenset([1,10]))
    # incompatibilidades.add(frozenset([1,2]))
    # incompatibilidades.add(frozenset([2,1]))
    # incompatibilidades.add(frozenset([1,10]))
    # incompatibilidades.add(frozenset([10,1]))
    # print(incompatibilidades)
    
    with open(ARCHIVO_PROBLEMA) as archivo:
        for linea in archivo:
            palabras = linea.split()
            match palabras[0]:
                case COMENTARIO:
                    print('comentario')
                case PROBLEMA:
                    print('definicion del problema')
                case INCOMPATIBILIDAD:
                    print('incompatibilidad')
                case TIEMPO_LAVADO:
                    print('tiempo de lavado')

if __name__ == "__main__":
    main()