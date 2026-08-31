from krypteringsAlgoritmer.cæsar import CæsarAlgorithm

def main():
    algorithm = CæsarAlgorithm(shift=3)
    print("Hello World!")
    print(algorithm.encrypt("Hello"))

# Sikrer at koden kun kjøres når filen kjøres direkte
if __name__ == "__main__":
    main()
