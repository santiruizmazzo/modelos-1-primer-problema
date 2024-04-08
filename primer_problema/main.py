def main() -> None:
    incompatibilidades = set([])
    incompatibilidades.add(frozenset([1,10]))
    incompatibilidades.add(frozenset([1,2]))
    incompatibilidades.add(frozenset([2,1]))
    incompatibilidades.add(frozenset([1,10]))
    incompatibilidades.add(frozenset([10,1]))
    print(incompatibilidades)

if __name__ == "__main__":
    main()