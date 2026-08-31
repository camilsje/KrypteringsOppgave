from constants import ALGORITHMS
from krypteringsAlgoritmer.cæsar import CæsarAlgorithm
from utils.les_fil import les_fil
from utils.skriv_fil import skriv_fil
import sys
from typing import Tuple


def avslutt(bruker_input):
    """Hjelpefunksjon som sjekker om brukeren vil avslutte"""
    if bruker_input.strip().lower() == 'q':
        print("Avslutter programmet....")
        sys.exit(0)

class UserInputHandler:
    def getFilsti(self) -> Tuple[str, str]:
        """
        Henter filstien basert på bruker input
        Returns:
            str: fil sti
            str: fil innhold
        """
        while True:
            file_sti = input("Skriv inn filnavnet til filen du vil kryptere/dekryptere: ")
            avslutt(file_sti)
            text = les_fil(file_sti)
            if text:
                return text, file_sti
            print("Ugyldig filsti. Vennligst prøv igjen.")

    def getAlgoritme(self) -> type:
        """
        Henter den riktige krypterings algoritmen fra en liste over tilgjengelige algoritmer.
        Returns:
            type: krypteringsAlgoritmen
            
        """
        tilgjengelige = list(ALGORITHMS.keys())
        print(f"Psst! Følgende algoritmer er tilgjengelige: {tilgjengelige}")
        
        while True:
            algoritme = input("Skriv inn algoritmen du vil bruke: ")
            avslutt(algoritme)
            if algoritme in ALGORITHMS:
                return ALGORITHMS[algoritme]
            print(f"Ugyldig valg. Vennligst velg en av disse: {tilgjengelige}\n")

    def getMetode(self) -> str:
        """
        Bruker velger om den vil dekryptere eller kryptere teksten
        Returns:
            str: d for dekryptering eller e for enkryptering.
        """
        while True:
            metode = input("Vil du dekryptere (d) eller kryptere (e)? ").casefold()
            avslutt(metode)
            if metode in ["d", "e"]:
                return metode
            print("Ugyldig valg. Du må skrive 'd' eller 'e'.\n")

    def getShift(self) -> int:
        """
        Brukeren velger hvor mange ganger den vil hoppe i alfabetet. 
        Returns:
            int: Antall hopp
        """
        while True:
            try:
                shift_input = input("Hvor mange bokstaver ønsker du å hoppe over? ")
                avslutt(shift_input)
                return int(shift_input)
                
            except ValueError:
                print("Ugyldig input. Vennligst skriv inn et heltall (f.eks. 7).\n")

    def skrive_til_fil(self, fil_sti: str, resultat: str):
        """
        Brukeren velger om den vil skrive resultatet til fil eller ikke
        """
        valg = input("\nVil skrive resultatet til den opprinnelige filen? (ja/nei): ").strip().lower()
        if valg in ["ja", "j"]:
            skriv_fil(fil_sti, resultat)
            print(f"Innholdet er skrevet til filen: {fil_sti}")

    def nyRunde(self):
        """
        Brukeren velger om den vil kryptere en ny fil eller avslutte programmet.
        """
        valg = input("\nVil du prøve med en ny fil? (ja/nei eller 'Q' for å avslutte): ").strip().lower()
        if valg in ['nei', 'n', 'q']:
            print("\nTakk for at du brukte programmet")
            sys.exit(0)
        print("\nStarter på nytt...\n" + "-"*20 + "\n")
        
        

