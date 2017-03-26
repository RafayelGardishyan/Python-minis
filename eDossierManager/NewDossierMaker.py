import time
time = 0
count = 1
while (time < 1):
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

    with open("Dossier " + name + " " + lname + " " + pc + ".txt", "w") as out_file:
        char = "1"
        for i in range(len(char)):
            out_string = name + "\n" + lname + "\n" + date + "\n" + pc + "\n" + oms + "\n" + bv + "\n" + zpc + "\n" + st + "\n" + prv + "\n" + adr + "\n" + comment
            out_file.write(out_string)

    count = count + 1
    
    
