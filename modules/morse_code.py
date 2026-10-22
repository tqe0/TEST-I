# made this because i had nothing else better to do
def main():
    # steal this random dictionary lmao
    morse_code_dictionary = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ',':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}

    options = {"option 1 ": "english > morse",
            "blank": "",
        "option 2 ": "morse > english"}

    reverse_dictionary = {v: k for k, v in morse_code_dictionary.items()}

    def printoptions(options):
        for k,v in options.items():
            if "blank" in k:
                print()
            else:
                print(f"\n{k}{v}")

    printoptions(options)

    user_choice = input("\n\nselect an option (1/2): \n") # more newlines chars = fix

    if user_choice == "1":
        user_text = input("enter english: ").strip()
        morse_code = ""

        for character in user_text.upper():
            if character == " ":
                morse_code += "/ "
            elif character in morse_code_dictionary:
                morse_code += morse_code_dictionary[character] + " "
            else:
                print(f"\nerror: can't translate '{character}'\n")
                return

        morse_decorator = "-" * len(morse_code.strip())

        print(f"\n{morse_decorator}")
        print(morse_code)
        print(f"{morse_decorator}\n")
    elif user_choice == "2":
        morse = input("enter morse: ")
        text = ""

        for part in morse.split():
            if part == "/":
                text += " "
            elif part in reverse_dictionary:
                text += reverse_dictionary[part]
            else:
                print(f"\nerror: can't translate '{part}'\n")
                return

        text_decorator = "-" * len(text.strip())
        print(f"\n{text_decorator}")
        print(text)
        print(f"{text_decorator}\n")
    else:
        print("\n1/2 wasnt selected\n")

if __name__ == "__main__":
    main()