from registry import ALGORITHMS
from utils.read_file import read_file
from utils.write_file import write_file
import sys
from typing import Tuple
from interfaces.algorithms import Encrypting


def terminate(user_input):
    """Hjelpefunksjon som sjekker om brukeren vil avslutte"""
    if user_input.strip().lower() == 'q':
        print("Avslutter programmet....")
        sys.exit(0)

class UserInputHandler:
    def get_file_path(self) -> Tuple[str, str]:
        """
        Henter filstien basert på bruker input
        Returns:
            str: fil sti
            str: fil innhold
        """
        while True:
            file_path = input("Skriv inn filnavnet til filen du vil kryptere/dekryptere: ")
            terminate(file_path)
            text = read_file(file_path)
            if text is not None: 
                return text, file_path
            print("Ugyldig filsti. Vennligst prøv igjen.")

    def get_algorithm(self) -> type[Encrypting]:
        """
        Henter den riktige krypterings algoritmen fra en liste over tilgjengelige algoritmer.
        Returns:
            type: krypteringsAlgoritmen
            
        """
        available_algorithms = list(ALGORITHMS.keys())
        print(f"Psst! Følgende algoritmer er tilgjengelige: {available_algorithms}")
        
        while True:
            algorithm = input("Skriv inn algoritmen du vil bruke: ")
            terminate(algorithm)
            if algorithm in ALGORITHMS:
                return ALGORITHMS[algorithm]
            print(f"Ugyldig valg. Vennligst velg en av disse: {available_algorithms}\n")

    def get_method(self) -> str:
        """
        Bruker velger om den vil dekryptere eller kryptere teksten
        Returns:
            str: d for dekryptering eller e for enkryptering.
        """
        while True:
            method = input("Vil du dekryptere (d) eller kryptere (e)? ").casefold()
            terminate(method)
            if method in ["d", "e"]:
                return method
            print("Ugyldig valg. Du må skrive 'd' eller 'e'.\n")

    def get_shift(self) -> int:
        """
        Brukeren velger hvor mange ganger den vil hoppe i alfabetet. 
        Returns:
            int: Antall hopp
        """
        while True:
            try:
                shift_input = input("Hvor mange bokstaver ønsker du å hoppe over? ")
                terminate(shift_input)
                return int(shift_input)
                
            except ValueError:
                print("Ugyldig input. Vennligst skriv inn et heltall (f.eks. 7).\n")

    def write_to_file(self, fil_sti: str, resultat: str):
        """
        Brukeren velger om den vil skrive resultatet til fil eller ikke
        """
        choice = input("\nVil skrive resultatet til den opprinnelige filen? (ja/nei): ").strip().lower()
        if choice in ["ja", "j"]:
            write_file(fil_sti, resultat)
            print(f"Innholdet er skrevet til filen: {fil_sti}")

    def new_round(self):
        """
        Brukeren velger om den vil kryptere en ny fil eller avslutte programmet.
        """
        choice = input("\nVil du prøve med en ny fil? (ja/nei eller 'Q' for å avslutte): ").strip().lower()
        if choice in ['nei', 'n', 'q']:
            print("\nTakk for at du brukte programmet")
            sys.exit(0)
        print("\nStarter på nytt...\n" + "-"*20 + "\n")
        
        

