import time
import os
import re

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

        print ("\033[0;35mIMPORTANT: Fractions will be ignored or result in an error\033[0m")
        choice = int ( float ( input ("Enter the number & Hit ENTER: ") ) )

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

    # Binary Conversions
    if (choice == 1):

        bi = int ( float ( input ("Enter a valid binary number: ") ) )
        flag = digitChecker(bi, choice)

        if (flag == 1):
            print ("\033[0;31mError: Binary number can only be a positive whole number and have digits 0 and 1\033[0m")
            navigation(choice)

        if (flag == 0):
            mySum1 = binaryToDecimal(bi)
            mySum2 = binaryToOctal(bi)
            mySum3 = binaryToHexadecimal(bi)

            if (bi == 0):
                conversionTitle()
                print("Decimal number: ", mySum1)
                print("Octal number: ", mySum2)
                print("Hexadecimal number: ", mySum3)
                navigation(choice)
            else:
                conversionTitle()
                print("Decimal number: ", mySum1)
                print("Octal number: ", mySum2)
                print("Hexadecimal number: ", mySum3)
                navigation(choice)

    # Decimal Conversions
    if (choice == 2):

        dec = int ( float ( input ("Enter a valid decimal number: ") ) )
        flag = digitChecker(dec, choice)

        if (flag == 1):
            print ("\033[0;31mError: Decimal number can only be a positive whole number and have digits between 0 and 9 inclusive \033[0m")
            navigation(choice)

        if (flag == 0):
            mySum1 = decimalToBinary(dec)
            mySum2 = decimalToOctal(dec)
            mySum3 = decimalToHexadecimal(dec)

            if (dec == 0):
                conversionTitle()
                print("Binary number: ", mySum1)
                print("Octal number: ", mySum2)
                print("Hexadecimal number: ", mySum3)
                navigation(choice)
            else:
                conversionTitle()
                print("Binary number: ", mySum1)
                print("Octal number: ", mySum2)
                print("Hexadecimal number: ", mySum3)
                navigation(choice)

    # Octal Conversions
    if (choice == 3):

        oct = int ( float ( input('Enter a valid octal number: ') ) )
        flag = digitChecker(oct, choice)

        if (flag == 1):
            print ("\033[0;31mError: Octal number can only be a positive whole number and have digits between 0 and 7 inclusive \033[0m")
            navigation(choice)

        if (flag == 0):
            mySum1 = octalToBinary(oct)
            mySum2 = octalToDecimal(oct)
            mySum3 = octalToHexadecimal(oct)

            if (oct == 0):
                conversionTitle()
                print("Binary number: ", mySum1)
                print("Decimal number: ", mySum2)
                print("Hexadecimal number: ", mySum3)
                navigation(choice)
            else:
                conversionTitle()
                print("Binary number: ", mySum1)
                print("Decimal number: ", mySum2)
                print("Hexadecimal number: ", mySum3)
                navigation(choice)

    # Hexadecimal Conversions
    if (choice == 4):

        hex = input("Enter a valid hexadecimal number: ")
        flag = digitChecker(hex, choice)

        if (flag == 1):
            print ("\033[0;31mError: Hexadecimal number can only be a positive whole number and have digits 0 to 9 and letters A to F inclusive \033[0m")
            navigation(choice)

        if (flag == 0):
            mySum1 = hexadecimalToBinary(hex)
            mySum2 = hexadecimalToDecimal(hex)
            mySum3 = hexadecimalToOctal(hex)

            print(hex)
            print(mySum2)

            conversionTitle()
            print("Binary number: ", mySum1)
            print("Decimal number: ", mySum2)
            print("Octal number: ", mySum3)
            navigation(choice)

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


        if (type(num) == str):
            # hexadecimal
            if (choice == 4):
                pattern = "[0-9a-fA-F]"

                for character in num:
                    if (not re.search(pattern, character)):
                        flag = 1
                        return flag
                return flag

        else:
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

def navigation (choice):
    print("\nDo you want to go back to the main menu?")
    decision = input("Type 'yes' to return to main menu or 'no' to reattempt: ")

    if (decision == "y" or decision == "Y" or decision == "yes" or decision == "Yes" or decision == "YES" or decision == "yEs" or decision == "yeS"):
        clearScreen()
        welcomeScreen()
    elif (decision == "n" or decision == "N" or decision == "no" or decision == "No" or decision == "NO" or decision == "nO"):
        userInput(choice)
    else:
        clearScreen()
        print("\033[0;31mError: Invalid input.\033[0m")
        navigation(choice)

# Binary Conversion Functions
def binaryToDecimal (bi):
    i = 0
    sum = 0

    while (bi != 0):

        rem = bi % 10
        bi = bi // 10
        sum = sum + rem * pow ( 2, i)
        i = i + 1

    return sum

def binaryToOctal (bi):

    octStr = ''
    octNum = 0

    dec = binaryToDecimal(bi)

    while (dec != 0):

        rem = dec % 8
        dec = dec // 8
        octStr = octStr + str(rem)

    octNum = reverseStrAndConvertToInt(octStr)
    return octNum

def binaryToHexadecimal (bi):

    dec = binaryToDecimal(bi)
    hexStr = decimalToHexadecimal(dec)

    return hexStr

# Decimal Conversion Functions
def decimalToBinary (dec):

    biStr = ''
    biNum = 0

    while (dec != 0):

        rem = dec % 2
        dec = dec // 2
        biStr = biStr + str(rem)

    biNum = reverseStrAndConvertToInt(biStr)
    return  biNum

def decimalToOctal (dec):

    octStr = ''
    octNum = 0

    while (dec != 0):

        rem = dec % 8
        dec = dec // 8
        octStr = octStr + str(rem)

    octNum = reverseStrAndConvertToInt(octStr)
    return octNum

def decimalToHexadecimal (dec):

    hexLetter = ''
    hexStr = ''
    hexNum = 0

    while (dec != 0):

        rem = dec % 16
        dec = dec // 16

        match rem:
            case 10:
                hexLetter = 'A'
            case 11:
                hexLetter = 'B'
            case 12:
                hexLetter = 'C'
            case 13:
                hexLetter = 'D'
            case 14:
                hexLetter = 'E'
            case 15:
                hexLetter = 'F'

        if (hexLetter != ''):
            hexStr = hexStr + hexLetter

        else:
            hexStr = hexStr + str(rem)

    hexStr = hexStr[::-1]
    return hexStr

# Octal Conversion Functions
def octalToBinary (oct):

    dec = octalToDecimal(oct)
    bi = decimalToBinary(dec)

    return  bi

def octalToDecimal (oct):

    sum = 0
    i = 0

    while (oct != 0):
        rem = oct % 10
        oct = oct // 10
        sum = sum + rem * pow (8, i)
        i = i + 1

    return sum

def octalToHexadecimal (oct):

    dec = octalToDecimal(oct)
    hex = decimalToHexadecimal(dec)

    return hex

# Hexadecimal Conversion Functions
def hexadecimalToDecimal (hex):

    hexNum = 0
    pattern1 = "[a-fA-F]"
    pattern2 = "[0-9]"
    sum = 0
    i = 0

    for character in hex:
        if re.search(pattern1, character):
            match character:
                case 'A':
                    hexNum = 10
                    sum = sum + hexNum * pow(16, i)
                case 'a':
                    hexNum = 10
                    sum = sum + hexNum * pow(16, i)
                case 'B':
                    hexNum = 11
                    sum = sum + hexNum * pow(16, i)
                case 'b':
                    hexNum = 11
                    sum = sum + hexNum * pow(16, i)
                case 'C':
                    hexNum = 12
                    sum = sum + hexNum * pow(16, i)
                case 'c':
                    hexNum = 12
                    sum = sum + hexNum * pow(16, i)
                case 'D':
                    hexNum = 13
                    sum = sum + hexNum * pow(16, i)
                case 'd':
                    hexNum = 13
                    sum = sum + hexNum * pow(16, i)
                case 'E':
                    hexNum = 14
                    sum = sum + hexNum * pow(16, i)
                case 'e':
                    hexNum = 14
                    sum = sum + hexNum * pow(16, i)
                case 'F':
                    hexNum = 15
                    sum = sum + hexNum * pow(16, i)
                case 'f':
                    hexNum = 15
                    sum = sum + hexNum * pow(16, i)
        elif re.search(pattern2, character):
            hexNum = int(character)
            sum = sum + hexNum * pow(16, i)
        i = i + 1
    return sum

def hexadecimalToBinary (hex):

    dec = hexadecimalToDecimal(hex)
    bin = decimalToBinary(dec)

    return bin

def hexadecimalToOctal (hex):

    dec = hexadecimalToDecimal(hex)
    oct = decimalToOctal(dec)

    return  oct

def reverseStrAndConvertToInt (strParam):
    reversedStr = strParam[::-1]
    return int (reversedStr)

def conversionTitle ():
    print('---------------------------------------------------------')
    print('>>> Converted Results ❤️  You\'re welcome 😊 <<<')
    print('---------------------------------------------------------')


def isolater(num):
    intNum = int(num)
    floatNum = float(intNum)
    fraction = num - floatNum

    return fraction

welcomeScreen()