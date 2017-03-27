import time
import glob, os
os.chdir("Dossiers")
while True:
    files = input('Wat is de naam en achternaam van het dossier (Voorbeeld: Jan Visser)')
    for file in glob.glob("Dossier " + files + "*"):
        print(file)
    filed = input('Wat is het registratienummer van het dossier (Voorbeeld: 5)')    
    f = open('Dossier ' + files + ' ' + filed, 'r')
    file_contents = f.read()
    print (file_contents)
    print ("\n\n\n")
    time.sleep(5)


