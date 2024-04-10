class TipoDeLinea():
  COMENTARIO = 'c'
  PROBLEMA = 'p'
  INCOMPATIBILIDAD = 'e'
  TIEMPO_LAVADO = 'n'

def cargar_problema_desde_archivo():
  ARCHIVO_PROBLEMA = 'primer_problema.txt'
  
  with open(ARCHIVO_PROBLEMA) as archivo:
    for linea in archivo:
      palabras = linea.split()
      match palabras[0]:
        case TipoDeLinea.COMENTARIO:
          print('comentario')
        case TipoDeLinea.PROBLEMA:
          print('definicion del problema')
        case TipoDeLinea.INCOMPATIBILIDAD:
          print('incompatibilidad')
        case TipoDeLinea.TIEMPO_LAVADO:
          print('tiempo de lavado')


def main() -> None:
  # incompatibilidades = set([])
  # incompatibilidades.add(frozenset([1,10]))
  # incompatibilidades.add(frozenset([1,2]))
  # incompatibilidades.add(frozenset([2,1]))
  # incompatibilidades.add(frozenset([1,10]))
  # incompatibilidades.add(frozenset([10,1]))
  # print(incompatibilidades)
  cargar_problema_desde_archivo()

if __name__ == "__main__":
  main()