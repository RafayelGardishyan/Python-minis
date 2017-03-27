while True:
    file = input('Wat is de naam en het registratienummer van het dossier (Voorbeeld: Jan Visser 5)')
    f = open('Dossiers/Dossier ' + file + ".txt", 'r')
    file_contents = f.read()
    print (file_contents)
    print ("\n\n\n")


