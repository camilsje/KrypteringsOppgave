from handlers.userInputHandler import UserInputHandler
import sys

def main():

    print("-" *20)
    print("VELKOMMEN TIL KRYPTERINGS-PROGRAMMET \n")
    print("Du kan når som helst avslutte ved å skrive 'Q'.")
    print("-" *20)

    userInput = UserInputHandler()

    while True:
        #1. Spør om fil
        text, file_path = userInput.getFilsti()

        #2. Spør om algoritme
        algorithm_class = userInput.getAlgoritme()

        #3.Spør om metode
        metode = userInput.getMetode()

        #4Spør om antall hopp, ved utvidelse må dette spørsmålet basere seg på hvilke algoritme det er. 
        shift = userInput.getShift()

        # Velger algoritme basert på brukerinput, standard brukerinput bør derfor være 
        # algoritme type og dekryptering/encryptering.
        algorithm = algorithm_class(shift=shift)
        if metode == "d":
            result = algorithm.decrypt(text)
        else:
            result = algorithm.encrypt(text)

        #5. Printer resultatet i terminalen
        print("-"*20)
        print("RESULTAT:")
        print(result)
        print("-"*20)

        #6. Skriver innholdet til filen, hvis ønskelig
        userInput.skrive_til_fil(file_path, f"\n\n Resultatet av krypteringen er: \n{result}")

        #6. Spør brukeren om den har noe mer den ønsker å kryptere
        userInput.nyRunde()


# Sikrer at koden kun kjøres når filen kjøres direkte
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgrammet ble avbrutt.")
        sys.exit(0)


