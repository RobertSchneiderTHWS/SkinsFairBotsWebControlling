import pathlib
import os

userInput = input("Enter Direction to correct: ")

windowsDir = pathlib.PureWindowsPath(userInput)

portableDir = windowsDir.as_posix()

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

addToClipBoard(portableDir)

print('Copied to Clipboard: '+portableDir)

