def write_file(file_path: str, text: str):
    try:
        with open(file_path, "a", encoding='utf-8') as file:
            file.write(text)
    except FileNotFoundError:
        print("Fant ikke filen du ønsker å skrive til")
    except Exception as e:
        print(f"Det oppstod en feil ved skrving {e}")


#For testing
# if __name__ == "__main__":
    #print(write_file("testFil.txt", "Hei"))