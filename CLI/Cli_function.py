import os 
import art
import shutil as sh
from CLI.ProjectFiles import FilesOct8
import termcolor as color
    
class ConfigUser:
    def __init__(self) -> None:
        self.Path = ""
        self.Projectname =""
        self.Activate = False
class ComandBase(ConfigUser):
    def __init__(self,Comand) -> None:
        self.Comand = Comand
        self.ListComands = ["SET PATH","NEW"]

    def Set_path(self,path,Config:ConfigUser = ConfigUser):
        Config.Path = path 

class CliFunctions:
    def __init__(self) -> None:
        
        self.StartProject = ConfigUser()
        self.Bases_ =ComandBase(self.StartProject)
        self.OctFiles =FilesOct8(None)
        self.Projects = []
    def Start(self):
        os.system("cls")
        art.tprint("\033 Oct8",space=3)
        color.cprint("Creating virtual environments with Oct8 CLI, start with the command for creating or editing projects, if you want help type help","yellow",attrs=["bold"])
        color.cprint("Welcome to Oct8 Cli","yellow")
        Comando = input("\033[0;32m> ")
        print("\033[0;0m")
        if(Comando =="break"):
           return 0
        else:
            self.ReturnComands(Comando)
        return Comando
    def ReturnComands(self,comands):
        if("SET PATH" == str(comands).upper()):
            Path = input("\033[0;32m What Path your Project? > ")
            self.Bases_.Set_path(Path,self.StartProject)


        if("NEW" == str(comands).upper()):
            if(self.StartProject.Path !=""):
                dir_path = os.path.dirname(os.path.realpath("Oct8Cli.py"))
                dir_path = dir_path+"\Oct8\Oct8"
                files = os.listdir(dir_path)
                for n_files in files:
                    sh.copy2(os.path.join(dir_path,n_files),self.StartProject.Path)
            else:
                color.cprint("Your Path local is empty","red")
                input(">..")

