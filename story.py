print ("We gaan een verhaaltje maken! Volg de instructies")
w1 = input("Zelfstandig naamwoord :")
w2 = input('Ander zelfstandig naamwoord :')
w3 = input("Werkwoord :")
w4 = input("Ander werkwoord :")
w5 = input("Bijvoeglijk naamwoord :")
w6 = input("Ander bijvoeglijk naamwoord :")
t = input("Kies de zin (type een getal tussen 1 en 4 in)")

if t == '1' :
    print ('De' + " " + w5 + " " + w1 + " " + 'ging' + " " + w3 + ' met ' + w6 + " " + w2 + " om te " + w4 + " ." )
elif t == '2' :
    print ('De' + " " + w6 + " " + w1 + " " + 'is gaan' + " " + w4 + ' met ' + w5 + " " + w2 + " en toen gingen ze " + w3 + " ." )
elif t == '3' :
    print (w1 + " " + 'was' + " een " + w5 + ' met een ' + w6 + " " + w2 + " die ging " + w4 + " ." )
elif t == '4' :
    print ('Op een mooie dag ging de '+ w5 + " " + w1 + " " + w3 + " in de " + w6 + " " + w2 + " waar de mensen " + w4 + " ." )

print ('Bedankt voor het gebruiken van deze app!')    

