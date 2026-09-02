from handlers.user_input_handler import UserInputHandler
import sys

def main():

    print("-" *20)
    print("VELKOMMEN TIL KRYPTERINGS-PROGRAMMET \n")
    print("Du kan når som helst avslutte ved å skrive 'Q'.")
    print("-" *20)

    input_handler = UserInputHandler()

    while True:
        #1. Spør om fil
        text, file_path = input_handler.get_file_path()

        #2. Spør om algoritme
        algorithm_class = input_handler.get_algorithm()

        #3.Spør om metode
        metode = input_handler.get_method()

        #4Spør om antall hopp, ved utvidelse må dette spørsmålet basere seg på hvilke algoritme det er. 
        shift = input_handler.get_shift()

        # Velger algoritme basert på brukerinput, standard brukerinput bør derfor være 
        # algoritme type og dekryptering/encryptering.
        algorithm = algorithm_class(shift=shift)
        if metode == "d":
            result = algorithm.decrypt(text)
        elif metode == "e":
            result = algorithm.encrypt(text)
        else:
            raise ValueError("Ugyldig metode. Velg 'd' for dekryptering eller 'e' for kryptering.")

        #5. Printer resultatet i terminalen
        print("-"*20)
        print("RESULTAT:")
        print(result)
        print("-"*20)

        #6. Skriver innholdet til filen, hvis ønskelig
        input_handler.write_to_file(file_path, f"\n\n Resultatet av krypteringen er: \n{result}")

        #6. Spør brukeren om den har noe mer den ønsker å kryptere
        input_handler.new_round()


# Sikrer at koden kun kjøres når filen kjøres direkte
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgrammet ble avbrutt.")
        sys.exit(0)


