import os 
import art
import termcolor as color

class CliFunctions:
    def Start(self):
        os.system("cls")
        art.tprint("\033 Oct8",space=3)
        color.cprint("Creating virtual environments with Oct8 CLI, start with the command for creating or editing projects, if you want help type help","yellow",attrs=["bold"])
        color.cprint("Welcome to Oct8 Cli","yellow")
        Comando = input("\033[0;32m> ")
        print("\033[0;0m")
        if(Comando =="break"):
           return 0
        return Comando