import random as r

def main():
    mock = mock_func(input('self explantory > '))
    mock_decorator = "-" * len(mock.strip()) # pretty dashes oooooooooo
    print(f"\n{mock_decorator}")
    print(f"{mock}")
    print(f"{mock_decorator}\n")

def mock_func(message):
    mock = ''
    use_upper = False

    for character in message:
        if not character.isalpha():
            mock += character
            continue
        if use_upper:
            mock += character.upper()
        else:
            mock += character.lower()

        if r.randint(1, 100) <= 90:
            use_upper = not use_upper
    return mock

if __name__ == "__main__":
    main()