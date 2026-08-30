from constants import ALFABETH

def encrypt_or_decrypt(tekst: str, shift: int, mode: str):
    """
    Velger om man vil kryptere eller dekryptere en tekst basert på mode parameteren 
    og sender tekst og shift til riktig funksjon
    Args:
        tekst (str): Teksten som skal krypteres eller dekrypteres
        shift (int): Antall plasser bokstavene skal flyttes
        mode (str): "e" for kryptering, "d" for dekryptering
    Returns:
        str: Den krypterte eller dekrypterte teksten
    """
    if (mode == "d"):
       return decrypt(tekst, shift)
    elif (mode.casefold ==  "e".casefold):
        return encrypt(tekst, shift)
    else:
        raise ValueError("Mode må være d (dekryptering) eller e (enkryptering)")


def encrypt(tekst: str, shift: int) -> str:
    """
    Krypterer en tekst ved å flytte bokstavene i teksten et gitt antall plasser i alfabetet.
    Args:
        tekst (str): Teksten som skal krypteres
        shift (int): Antall plasser bokstavene skal flyttes
    Returns:
        str: Den krypterte teksten
    """
    new_text = ""
    for char in tekst:
        if char.isupper():
            position = ALFABETH.index(char)
            new_index = ((position + shift)%29)
            new_char = ALFABETH[new_index]
            new_text += new_char
        elif char.islower():
            position = ALFABETH.index(char.upper())
            new_index = ((position + shift)%29)
            new_char = ALFABETH[new_index]
            new_text += new_char
        else:
            new_text += char
    return new_text

def decrypt(tekst: str, shift: int) -> str:
    """
    Dekrypterer en tekst ved å flytte bokstavene i teksten et gitt antall plasser tilbake i alfabetet.
    Args:
        tekst (str): Teksten som skal dekrypteres
        shift (int): Antall plasser bokstavene skal flyttes tilbake
    Returns:
        str: Den dekrypterte teksten
    """
    new_text = ""
    for char in tekst:
        if char.isupper():
            position = ALFABETH.index(char)
            new_index = ((position - shift)%29)
            new_char = ALFABETH[new_index]
            new_text += new_char
        elif char.islower():
            position = ALFABETH.index(char.upper())
            new_index = ((position - shift)%29)
            new_char = ALFABETH[new_index]
            new_text += new_char.lower()
        else:
            new_text += char
    return new_text

print(encrypt_or_decrypt("Hello", 3, "d"))
        


