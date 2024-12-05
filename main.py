from karlib.boxify import boxify

import libs.exporters
import libs.fetchers
import libs.loaders

def mainmenu():
    while True:
        menu = """\
        [1] Connect to database
        [2] Settings
        [3] Exit"""
        print(boxify(menu))

        choice = input("Enter your choice >> ")
        choice = choice.strip()

        if not choice in [str(i) for i in range(1, menu.count("\n") + 2)]:
            print("Please enter a valid choice.")
            continue

        match choice:
            case "1":
                return "connectdb"
            case "2":
                return "settings"
            case "3":
                exit()

        break

def main():
    main_welcome_string = libs.loaders.load_asciiart("EMySQL")
    print(boxify(main_welcome_string), end="\n\n")

    operation = mainmenu()

    match operation:
        case "connectdb":
            pass
        case "settings":
            pass

if __name__ == "__main__":
    main()