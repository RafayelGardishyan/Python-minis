while True:
    file = input('Wat is het naam en het paspoortcode van het dossier (Voorbeeld: Jan Visser AB1234567)')
    f = open('Dossier ' + file + ".txt", 'r')
    file_contents = f.read()
    print (file_contents)
    print ("\n\n\n")


