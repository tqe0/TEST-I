from modules import mock_people
from modules import morse_code

TOOLS = {
    "1": ("mock text", mock_people.main),
    "2": ("morse code", morse_code.main), # frick u and ur "ohh but u add commas to the end of ur dics" let me live bro its called maintainability !!!!!!!
}

def main():
    while True:
        lines = ["select a tool:"]
        for key, (name, _) in TOOLS.items():
            lines.append(f"\n  {key}. {name}\n")
        lines.append("\n  q. quit") # should i add another newline char here???
        print("\n".join(lines))

        choice = input("> ").strip().lower()

        if choice == "q":
            break
        elif choice in TOOLS:
            name, func = TOOLS[choice]
            print(f"\nselected: {name}\n")
            func()
        else:
            print("\ninvalid choice\n")

if __name__ == "__main__":
    main()