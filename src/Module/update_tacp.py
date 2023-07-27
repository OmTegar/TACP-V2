def update_tacp():
    import os
    print("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in ['Y', 'y']:
        os.system("git clone --single-branch --branch DEVELOPMENT https://github.com/OmTegar/TACP-V2.git")
        os.system("cd TACP-V2 && sudo bash ./src/update.sh")
        os.system("tacp")