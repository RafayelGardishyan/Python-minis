import os, sys
import glob
import time
os.chdir("Dossiers")
while True:
    # listing directories
    print ("De naam en de achternaam van het persoon:")
    files = input()
    for file in glob.glob("Dossier " + files + "*"):
        print(file)
    print ("Het registratienummer het persoon:")
    pc = input()
    os.remove("Dossier " + files + " " + pc)

    print ("Succesvol verwijderd \n\n")
    time.sleep(5)
