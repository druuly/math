import time
import os

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def arithmetic_sequence(n, i, option):
    result = 0
    for x in range(i, n + 1):
        result += 4 * x ** 2
        if option.lower() == "y":
            time.sleep(0.01)
            print("Performed --> 4*(", x, "^2)")
            print("=", 4 * x ** 2)
    if option.lower() == "y":
        print("Now Add Them Together: ")
    print("Summation: ", result)
    input("\nPress Any Key To Continue...")
    clear()

def menu():
    try:

        n = int(input("Welcome to Arithemtic Series. "
                    "\n Input Last Index Value: "))
        i = int(input(" Input First Index Value: "))
        if n > i:
            option = str(input("\nThe Base Equation Will Be: 4r^2. \n"
                            "Feel Free To Change Code For Different Equation. \n"
                            "\n Would you like to see the operations being performed?\n"
                            "(Y/N)?: "))
            clear()
            arithmetic_sequence(n, i, option)
        else:
            input("N must be less than I. \n"
                "Press Enter To Continue")
    except ValueError:
        clear()
        input("Invalid input. Please enter integers for N and I.\nPress Enter To Continue")
        clear()
    except Exception:
        clear()
        input("An error has occured. Press any key to continue...")
        clear()

while True: menu()
