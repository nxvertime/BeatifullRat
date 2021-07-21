from colorama import *
from os import name, system, getenv
import socket
from time import sleep

from optparse import OptionParser
## set the clear command by os name
if name == 'nt': ## windows
    def clear():
        system('cls')
else: ## linux distrib.
    def clear():
        system('clear')




## init colorama to dodge the problems
init()

## set colors more simple :)

red = Fore.RED
lightRed = Fore.LIGHTRED_EX

blue = Fore.BLUE
lightBlue = Fore.LIGHTBLUE_EX

green = Fore.GREEN
lightGreen = Fore.LIGHTGREEN_EX

yellow = Fore.YELLOW
lightYellow = Fore.LIGHTYELLOW_EX

magenta = Fore.MAGENTA
lightMagenta = Fore.LIGHTMAGENTA_EX

cyan = Fore.CYAN
lightCyan = Fore.LIGHTCYAN_EX

white = Fore.RESET

black = Fore.BLACK

reset = Fore.RESET

## set usefull vars

attention = f'{reset}[{yellow}!{reset}] '
info = f'{reset}[{cyan}*{reset}] '
ok = f'{reset}[{lightGreen}ok{reset}] '
success = f'{reset}[{green}v{reset}] '
error = f'{reset}[{yellow}!{reset}] '
question = f'{reset}[{lightGreen}?{reset}] '
## functions of modes
def server():
    system("title Beatifull Rat Server    github.com/nxvertime")
    clear()
    print(f"{info}Server mode")
    
def build():
    system("title Beatifull Rat Builder    github.com/nxvertime")
    clear()
    print(f"{info}Build a rat")
    print(f"{info}Please enter the file name:")
    file_name = str(input(f"{magenta}>{cyan}"))
    reset
    if len(file_name) == 0:
        print(f"{error}Filename too short ! (1 char min)")
        sleep(3)
        return
    elif len(file_name) > 19:
        print(f"{error}File name too long ! (19 chars max)")
        sleep(3)
        return
    print(f"{ok}The file name is set on: \"{file_name}\"")
    print(f"{info}Enter a port:")
    port = int(input(f"{magenta}>{cyan}"))
    if len(str(port)) > 4:
        print(f"{error}Port too long! (4 numbers max)")
        sleep(3)
        return
    else:
        pass
    reset
    print(f"{ok}Port is set on \"{port}\"")
    print(f"{question}Do you want to compile it as a .exe?")
    rep_comp = str(input(f"{magenta}>{cyan}"))
    reset
    if rep_comp == "yes" or "y" or "Y" or "Yes":
        compile = True
    elif rep_comp == "no" or "n" or "N" or "No":
        compile = False
    else:
        print(f"{error}Bad answer :/")
        sleep(3)

def main():
    system("title Beatifull Rat Menu    github.com/nxvertime")
    clear()
    print(f"{info}Beautifull Rat by nxvertime")
    print(f"{attention}github.com/nxvertime")
    print(f"{info}Choose an option:"
          f"\n    [{cyan}1{reset}]  {magenta}Build a rat{reset}"
          f"\n    [{cyan}2{reset}]  {magenta}Run a server{reset}")
    try:
        mode = int(input(f"{magenta}>{cyan}"))
        if mode == 1:
            build()
        elif mode == 2:
            server()
        else:
            print(f"{error}Bad answer :/")
            sleep(3)
    except ValueError as e:
        print(f"{error}{e}")
        sleep(3)
    reset

while True:
    main()