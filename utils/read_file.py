def read_file(file_path: str ) -> str | None:
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
        return None
    except Exception as e:
        print(f"Det oppstod en feil ved lesing {e}")
        return None


#For testing
# if __name__ == "__main__":
    #print(read_file("testFil.txt", "Hei"))