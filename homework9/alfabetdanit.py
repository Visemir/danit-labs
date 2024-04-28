class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def letters_num(self):
        return len(self.letters)

    def letters_print(self):
        print(" ".join(self.letters))

class EngAlphabet(Alphabet):
    _letters_num = None
    language = "EN"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        super().__init__(self.language, self.letters)
        EngAlphabet._letters_num = len(self.letters)

    

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return f"Літера {letter} належить до англійського алфавіту"
        else:
            return f"Літера {letter} не належить до англійського алфавіту"
    
    def letters_num(self):
        return self._letters_num
    
    @staticmethod
    def example():
        return "This is the ninth homework in the DEVOPS course at Danit Academy."

def main():
# Тести
    any_letters=None
    eng = EngAlphabet()
    
    print("Літери Англійського алфавіту:")
    eng.letters_print()

    print(f"Кількість літер у {eng.language} алфавіті :", eng.letters_num())

    

    while True:
        while True:
            letter_to_check = input("Введіть літеру для перевірки: ")
            if len(letter_to_check) == 1 and letter_to_check.isalpha():
                break    
            else:
                print("Будь ласка, введіть лише одну літеру.")
                
        print(eng.is_en_letter(letter_to_check))
        answer = input("Чи потрібно ще перевірити? (Y/N): ")
        if answer.lower() != 'y':
            break


    print("Приклад тексту англійською мовою:", EngAlphabet.example())

    any_letters = input("Введіть літери будь-якого алфавіту: ")
    lang =  input("Введіть мову цього алфавіту: ")
    any_alphabet = Alphabet(lang, any_letters)
    print(f"Кількість літер у {any_alphabet.lang} алфавіті :", any_alphabet.letters_num())
    print(f"Літери алфавіту {any_alphabet.lang}:")
    any_alphabet.letters_print()

if __name__ == "__main__":
    main()