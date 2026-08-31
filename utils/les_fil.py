def les_fil(file_path: str ) -> str:
    """
    Leser innholdet i en fil
    Args:
        Filstien (str)
    Returns:
        Filinnholdet (str)
    """
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print (f"Fant ikke filen: {file_path}. Sjekk filbanen")
    except Exception as e:
        print(f"Det oppstod en feil ved lesing {e}")


"""
For å teste funksjonen kommenter ut.
"""
#print(les_fil("testFil.txt"))