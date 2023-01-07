#!/usr/bin/python

# Import required library.
import os
import modules.my_functions as menu

# Defien the main function.
def main():
    os.system("clear")
    userOptions = {1:"Creat a Json file for Douglas College weather",
                   2:"Print the next 6 hours forecast temperature for given longitude and latitude",
                   3:"Exit"}
    menu.showBanner()

    while(True):
        menu.printMenu(userOptions)
        userOption = ''
        try:
            userOption = int(input('Enter your choice >>'))
        except:
            print("Wrong input. Please enter a number.")

        if userOption == 1:
            menu.option1()
        elif userOption == 2:
            menu.option2()
        elif userOption == 3:
            print("Thank you bye.")
            exit()
        else:
            print("Invalid input. Please input integer from 1-3.")

if __name__ == "__main__":
    main()