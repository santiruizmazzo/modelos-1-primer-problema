import pprint

class TipoDeLinea():
  COMENTARIO = 'c'
  PROBLEMA = 'p'
  INCOMPATIBILIDAD = 'e'
  TIEMPO_LAVADO = 'n'

def cargar_problema_desde_archivo():
  ARCHIVO_PROBLEMA = 'primer_problema.txt'
  
  with open(ARCHIVO_PROBLEMA) as archivo:
    linea = archivo.readline().split()
    
    while linea[0] != TipoDeLinea.PROBLEMA:
      linea = archivo.readline().split()
    
    cantidad_prendas = int(linea[2])
    cantidad_incompatibilidades = int(linea[3])

    prendas = []
    incompatibilidades = {k: [] for k in range(1, cantidad_prendas+1)}

    for linea in archivo:
      palabras = linea.split()
      match palabras[0]:
        case TipoDeLinea.COMENTARIO:
          print('comentario')
        case TipoDeLinea.PROBLEMA:
          print('definicion del problema')
        case TipoDeLinea.INCOMPATIBILIDAD:
          incompatibilidades[int(palabras[1])].append(int(palabras[2]))
        case TipoDeLinea.TIEMPO_LAVADO:
          prendas.append((int(palabras[1]), int(palabras[2])))
    
    prendas.sort(reverse=True, key=lambda e: e[1])
    return prendas, incompatibilidades

def main() -> None:
  prendas, incompatibilidades = cargar_problema_desde_archivo()
  pprint.pprint(prendas)
  # pprint.pprint(incompatibilidades)

if __name__ == "__main__":
  main()