import pyautogui
import time
import sys
import os

enter = True
integer = False
countdown = 10

def help():
    print('''
    Command Help:
            type ">>clear" to clear the console
            type ">>quit" to quit
            type ">>enter" to toggle whether the enter button is pressed between typing
            type ">>toggles" to show all toggles, e.g. enter
            type ">>countdown!" to change the amount of time before it starts spamming out of inputs (the normally 10 second countdown)
    
    How to use the autospammer:
            first input: type what should be repeated
            second input: type how many times the text should be repeated
            wait for the countdown to be completed, and it will start
''')
    input(f"\n\n\n\n\npress enter to continue")


while True:
    command = input("Press enter to continue, or type a command, type >>helpMe for more: ")
    if command.lower() == '>>helpme':
        help()
    elif command.lower() == '>>clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif command.lower() == '>>quit':
        sys.exit("Exiting... Goodbye :)")
    elif command.lower() == '>>enter':
        if enter:
            enter = False
        else:
            enter = True
        print(f"Enter: {enter}")
    elif command.lower() == '>>toggles':
        print(f"Enter: {enter}\nMore toggles come soon...")
    elif command.lower() == '>>countdown':
        integer = False
        countdown = int(input("How long should the countdown be? "))

    text = input("What should I type? ")
    amount = int(input("How many times? "))

    for i in range(countdown):
        print(countdown-i)
        time.sleep(1)
    for i in range(amount):
        pyautogui.write(text, interval=0)
        if enter:
            pyautogui.press('enter')