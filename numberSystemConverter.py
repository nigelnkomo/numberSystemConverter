import time

def welcomeScreen ():

    while True:
        print ('---------------------------------------------------------')
        print ('>>> Welcome to the Number System Converter Program 😊 <<<')
        print ('---------------------------------------------------------')

        print(">> Select Conversion Type: ")
        print("> 1. Binary Conversion")
        print("> 2. Decimal Conversion")
        print("> 3. Octal Conversion")
        print("> 4. Hexadecimal Conversion")
        print("> 5. Exit the Program \n")

        choice = int ( input ("Enter the number & Hit ENTER: "))

        match choice:
            case 1:
                userInput(1)
                break
            case 2:
                userInput(2)
                break
            case 3:
                userInput(3)
                break
            case 4:
                userInput(4)
                break
            case 5:
                quit()
            case _:
                print("\033[0;31mError: The number must be between 1 and 5 inclusive\033[0m")
                print("Waiting 5 secs before continuing...")
                time.sleep(5)
                continue


def userInput (choice):
    print (choice)

welcomeScreen()