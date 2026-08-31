from constants import ALPHABET
from interfaces.algorithms import Encrypting

class CæsarAlgorithm(Encrypting):
    def __init__(self, shift: int):
        """
        Intialiserer CæsarAlgorithm med et gitt skift og alfabetet.
        Arg:
            shift (int): Antall plasser bokstavene skal flyttes i alfabetet
        """
        self.alfabeth = ALPHABET 
        self.shift = int(shift)
    
        
    def encrypt(self, text: str) -> str:
        """
        Krypterer en tekst ved å flytte bokstavene i teksten et gitt antall plasser i alfabetet.
        Args:
            tekst (str): Teksten som skal krypteres
            shift (int): Antall plasser bokstavene skal flyttes
        Returns:
            str: Den krypterte teksten
        """
        return _shift_char(text, self.shift)

    def decrypt(self, text: str) -> str:
        """
        Dekrypterer en tekst ved å flytte bokstavene i teksten et gitt antall plasser tilbake i alfabetet.
        Args:
            tekst (str): Teksten som skal dekrypteres
            shift (int): Antall plasser bokstavene skal flyttes tilbake
        Returns:
            str: Den dekrypterte teksten
        """
        return _shift_char(text, -self.shift)

  
        

def _shift_char(text: str, shift: int) -> str:
    """
    Privat Hjelpemetode 
    Flytter bokstavene i teksten et gitt antall plasser i alfabetet
    Args:
        tekst (str): Teksten som skal krypteres eller dekrypteres
        shift (int): Antall plasser bokstavene skal flyttes
    Returns:
    """
    new_text = ""
    for char in text:
        if char.isupper():
            position = ALPHABET.index(char)
            new_index = ((position + shift)%len(ALPHABET))
            new_char = ALPHABET[new_index]
            new_text += new_char
        elif char.islower():
            position = ALPHABET.index(char.upper())
            new_index = ((position + shift)%len(ALPHABET))
            new_char = ALPHABET[new_index]
            new_text += new_char.lower()
        else:
            new_text += char
    return new_text


# I cæsar.py – legg til på slutten
"""
if __name__ == "__main__":
    cipher = CæsarAlgorithm(shift=3)
    encrypted = cipher.encrypt("Hello")
    print(f"Encrypted: {encrypted}")
    
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
"""