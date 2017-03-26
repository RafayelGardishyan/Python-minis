import os, sys
while True:
    # listing directories
    print ("De naam en de achternaam van het persoon:")
    name = input()
    print ("De paspoortnummer het persoon:")
    pc = input()

    # removing
    os.remove("Dossier " + name + " " + pc + ".txt")

    print ("Succesfol vervijderd \n\n")
