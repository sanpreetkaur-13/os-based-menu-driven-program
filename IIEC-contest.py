import os
print("***************************************Hello! How can SANS help you?********************************************")
print()
while True:   
    print("*************************************What Program would you like to open?****************************************")
    p = input()
    if(("run" in p) or ("open" in p) or ("launch" in p)) and (("browser" in p) or ("explorer" in p)):
        print("Opening a Browser!")
        os.system("iexplore")
    elif(("run" in p) or ("open" in p) or ("launch" in p)) and (("mediaplayer" in p) or ("songplayer" in p)):
        print("Opening Media Player!")
        os.system("wmplayer")
    elif(("run" in p) or ("open" in p) or ("launch" in p)) and (("notepad" in p)or("editor" in p)):
        print("Opening Text Editor! ")
        os.system("notepad")
    elif (("open" in p) or ("run" in p) or ("launch" in p)) and ("calculator" in p):
        print("Opening Calculator")
        os.system("calc")    
    elif(("run" in p) or ("open" in p) or ("launch" in p)) and (("jupyter" in p)or("IDE" in p)):
        print("Opening Jupyter IDE")
        os.system("jupyter notebook")
    elif(("run" in p) or ("open" in p) or ("launch" in p)) and (("paint" in p) or ("drawing software" in p)):
        print("Opening Paint Software!")
        os.system("mspaint")
    elif(("run" in p) or ("open" in p) or ("launch" in p)) and ("gitbash" in p):
        print("Opening Git Bash")
        os.system("git bash")
    elif(("run" in p) or ("open" in p) or ("launch" in p)) and ("chrome" in p):
        print("Opening the Chrome Browser")
        os.system("Chrome")             
    elif("exit" in p) or ("break" in p):
        print("You requested to close the program")
        print(".........----------********----------..........")
        break
    else:
        print("Program not found")
    