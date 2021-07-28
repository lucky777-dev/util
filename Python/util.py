import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def askIntRange(min, max):
    choice = input()
    while not choice.isdigit():
        choice = input("Please enter a valid number: ")
    while int(choice) < min or int(choice) > max:
        choice = input(f"Please enter a number between {min} and {max}: ")
        while not choice.isdigit():
            choice = input("Please enter a valid number: ")
    return int(choice)

def fileExist(fileName):
    return os.path.exists(os.getcwd() + fileName)

def loadFile(path)):
    if not fileExist(os.getcwd() + path):
        createConfig()
    else:
        load = []
        with open(os.getcwd() + path, 'r') as file:
            for line in file:
                load.append(line)
    return load

def writeFile(path):
    with open(os.getcwd() + path, 'w') as file:
        file.write("Something..")