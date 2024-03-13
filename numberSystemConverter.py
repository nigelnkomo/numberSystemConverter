import time
import os

def welcomeScreen ():

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
            case 2:
                userInput(2)
            case 3:
                userInput(3)
            case 4:
                userInput(4)
            case 5:
                quit()
            case _:
                print("\033[0;31mError: The number must be between 1 and 5 inclusive\033[0m")
                print("Waiting 5 secs before continuing...")
                time.sleep(5)
                clearScreen()
                print("\033[0;31mMake sure your number is between 1 and 5 inclusive ❗\033[0m")
                welcomeScreen()


def userInput (choice):
    clearScreen()
    mySum = 0

    if (choice == 1):

        bi = int ( input ("Enter a valid binary number: ") )
        flag = digitChecker(bi, choice)

        if (flag == 1):
            print ("\033[0;31mError: Binary can only be positive and have digits 0 and 1\033[0m")
            navigation()

        if (flag == 0):
            mySum = binaryToDecimal(bi)
            
            if (bi == 0):
                print("Decimal number: ", mySum)
                print()
            else:
                print("Decimal number: ", mySum)
                print()


def clearScreen ():
    # Windows
    if os.name == 'nt':
        os.system('cls')

    # Linux & MacOS
    else:
        os.system('clear')

def digitChecker(num, choice):

    flag = 0

    while (True):

        rem = num % 10

        # binary
        if ((rem == 0 or rem == 1) and choice == 1):
            return flag
        # decimal
        elif ((rem >= 0 and rem <= 9) and choice == 2):
            return flag
        # octal
        elif ((rem >= 0 and rem <=7) and choice == 3):
            return flag
        else:
            flag = 1
            return flag

def navigation ():
    print("\nDo you want to go back to the main menu?")
    decision = input("Type y to proceed with binary conversion or n to return to main menu: ")

    if (decision == "y" or decision == "Y" or decision == "yes" or decision == "Yes" or decision == "YES" or decision == "yEs" or decision == "yeS"):
        userInput(1)
    if (decision == "n" or decision == "N" or decision == "no" or decision == "No" or decision == "NO" or decision == "nO"):
        clearScreen()
        welcomeScreen()

def binaryToDecimal (bi):
    i = 0
    sum = 0

    while (bi != 0):

        rem = bi % 10
        bi = bi // 10
        sum = sum + rem * pow ( 2, i)
        i = i + 1

    return sum

welcomeScreen()