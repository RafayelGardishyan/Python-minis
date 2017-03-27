import os, sys
while True:
    # listing directories
    print ("De naam en de achternaam van het persoon:")
    name = input()
    print ("Het registratienummer het persoon:")
    pc = input()


    os.remove("Dossiers/Dossier " + name + " " + pc + ".txt")

    print ("Succesvol verwijderd \n\n")
