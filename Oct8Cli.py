import os 
import art
import termcolor as color
from CLI.Cli_function import CliFunctions
def main():
    cli_param = CliFunctions()
    while(True):
        if(cli_param.Start()==0):
            break
        else:
            pass


main()