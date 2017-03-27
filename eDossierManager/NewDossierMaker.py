import time
tide = 0
count = 1
while (tide < 1):
    with open("regn.txt", "w") as out_regn:
       char = "1"
       for i in range(len(char)):
            out_string = str(regn)
            out_regn.write(out_string)
    
    regn = regn + 1	
    file = 'regn.txt'
    f = open(file)
    file_contents = f.read()
    
    regnn = file_contents
    name = input("Naam: ")
    lname = input("Achternaam: ")
    date = input("Geboortedatum: ")
    pc = input("Paspoortnummer: ")
    oms = input("Omschrijving: ")
    bv = input("Werkt / Studeert bij:")
    zpc = input("Postcode: ")
    st = input("Woonplaats: ")
    prv = input("Provincie: ")
    adr = input("Adres: ")
    comment = input("Comentaar: ")

    with open("Dossiers/Dossier " + name + " " + lname + " " +  regnn + ".txt", "w") as out_file:
        char = "1"
        for i in range(len(char)):
            out_string = regnn + "\n" + name + "\n" + lname + "\n" + date + "\n" + pc + "\n" + oms + "\n" + bv + "\n" + zpc + "\n" + st + "\n" + prv + "\n" + adr + "\n" + comment
            out_file.write(out_string)

    count = count + 1
    print ("\n\n" + "De registratienummer is " + regnn + '\n\n')
    time.sleep (5)

