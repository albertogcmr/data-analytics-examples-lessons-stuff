from modules.reading import open_textfile
from modules.saving import save_textfile


INPUT_FILE = './texts/textfile.txt'
OUTPUT_FILE = './texts/textfile2.txt'

def main(): 
    text = open_textfile(INPUT_FILE)
    print(text)
    save_textfile(text, OUTPUT_FILE)

    


if __name__ == "__main__":
    main()