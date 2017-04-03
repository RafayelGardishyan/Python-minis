import time
import datetime
d = datetime.date.today()
dm = d.month
dd = d.day

print ('Welkom bij TheCoiner')

file = 'data/monthday/month.txt'
f = open(file)
file_contents = f.read()
pdm = file_contents

file = 'data/monthday/day.txt'
f = open(file)
file_contents = f.read()
pdd = file_contents                

file = 'data/coins/dailycoins.txt'
f = open(file)
file_contents = f.read()

tc = file_contents
with open("data/monthday/month.txt", "w") as out_month:
           char = "1"
           for i in range(len(char)):
                out_string = str(dm)
                out_month.write(out_string)

with open("data/monthday/day.txt", "w") as out_day:
           char = "1"
           for i in range(len(char)):
                out_string = str(dd)
                out_day.write(out_string)
               
if int(dm) > int(pdm):
    print('Je hebt ' + tc + ' munt(en) gekregen')
    file = 'data/coins/coins.txt'
    f = open(file)
    file_contents = f.read()
    coins = file_contents
    coins = int(coins) + int(tc)
    coins = str(coins)
    
    with open("data/coins/coins.txt", "w") as out_coins:
           char = "1"
           for i in range(len(char)):
                out_string = str(coins)
                out_coins.write(out_string)
                
    file = 'data/coins/coins.txt'
    f = open(file)
    file_contents = f.read()
    coins = file_contents

    print('Je hebt ' + coins + ' munten')
else :
     if int(dd) > int(pdd):
           print('Je hebt ' + tc + ' munt(en) gekregen')
           file = 'data/coins/coins.txt'
           f = open(file)
           file_contents = f.read()
           coins = file_contents
           coins = int(coins) + 1
           coins = str(coins)
    
           with open("data/coins/coins.txt", "w") as out_coins :
                  char = "1"
                  for i in range(len(char)):
                       out_string = str(coins)
                       out_coins.write(out_string)
                
           file = 'data/coins/coins.txt'
           f = open(file)
           file_contents = f.read()
           coins = file_contents

           print('Je hebt ' + coins + ' munten')

     else:
          print("Je hebt vandaag al munt(en) gekregen")
          
          file = 'data/coins/coins.txt'
          f = open(file)
          file_contents = f.read()
          coins = file_contents
          coins = str(coins)
          
          print('Je hebt ' + coins + ' munten')

coins = int(coins)
if coins  >  1:
    while (coins != 1):
         print("Je kan de volgende dingen kopen \n 1. Geldboom = 2 munten (+1) \n 2. Oma = 5 munten (+5) \n 3. Spaarvarken 15 munten(+10)")
         ch = input()
         if ch == 1:
             coins = int(coins)- 2
             with open("data/coins/coins.txt", "w") as out_coins:
              char = "1"
              for i in range(len(char)):
                out_string = str(coins)
                out_coins.write(out_string)
                
             file = 'data/coins/coins.txt'
             f = open(file)
             file_contents = f.read()
             coins = file_contents
             print("Je hebt nu " + coins + " munten")
            
             tc = int(tc) + 1
             with open("data/coins/dailycoins.txt", "w") as out_dc:
               char = "1"
               for i in range(len(char)):
                    out_string = str(tc)
                    out_dc.write(out_string)
                    
               file = 'data/items/mt.txt'
               f = open(file)
               file_contents = f.read()
               pb = file_contents
               pb = int(pb)+ 1
               
               with open("data/items/mt.txt", "w") as out_mt:
                   char = "1"
                   for i in range(len(char)):
                        out_string = str(coins)
                        out_mt.write(out_string)     
                    
               file = 'data/coins/dailycoins.txt'
               f = open(file)
               file_contents = f.read()
               tc = file_contents
              
               print("Je hebt een Geldboom gekocht je krijgt nu " + tc + " munten per dag. Je balans is: " + coins + " munten.")
               print("Wil je nog iets anders kopen ?")
         elif ch == 3:
              coins = int(coins)-15
              with open("data/coins/coins.txt", "w") as out_coins:
                  char = "1"
                  for i in range(len(char)):
                      out_string = str(coins)
                      out_coins.write(out_string)
                
              file = 'data/coins/coins.txt'
              f = open(file)
              file_contents = f.read()
              coins = file_contents
              print("Je hebt nu " + coins + " munten")
              tc = int(tc) + 5
              with open("data/coins/dailycoins.txt", "w") as out_dc:
               char = "1"
               for i in range(len(char)):
                    out_string = str(tc)
                    out_dc.write(out_string)

               
               file = 'data/items/pb.txt'
               f = open(file)
               file_contents = f.read()
               pb = file_contents
               pb = int(pb)+ 1
               
               with open("data/items/pb.txt", "w") as out_pb:
                    char = "1"
                    for i in range(len(char)):
                         out_string = str(coins)
                         out_pb.write(out_string)     
                    
              file = 'data/coins/dailycoins.txt'
              f = open(file)
              file_contents = f.read()
              tc = file_contents
              
              print("Je hebt een Spaarvarken gekocht je krijgt nu " + tc + " munten per dag. Je balans is: " + coins + " munten.")
              print("Wil je nog iets anders kopen ?")
         elif ch == 2:
              coins = int(coins)-5
              with open("data/coins/coins.txt", "w") as out_coins:
                  char = "1"
                  for i in range(len(char)):
                      out_string = str(coins)
                      out_coins.write(out_string)
                
              file = 'data/coins/coins.txt'
              f = open(file)
              file_contents = f.read()
              coins = file_contents
              print("Je hebt nu " + coins + " muntren")
              tc = int(tc) + 10
              with open("data/coins/dailycoins.txt", "w") as out_dc:
                   char = "1"
                   for i in range(len(char)):
                         out_string = str(tc)
                         out_dc.write(out_string)
               
              file = 'data/items/gm.txt'
              f = open(file)
              file_contents = f.read()
              pb = file_contents
              pb = int(pb)+ 1
               
              with open("data/items/gm.txt", "w") as out_gm:
                   char = "1"
                   for i in range(len(char)):
                        out_string = str(coins)
                        out_gm.write(out_string)          
                    
              file = 'data/coins/dailycoins.txt'
              f = open(file)
              file_contents = f.read()
              tc = file_contents
                        
              print("Je hebt een Oma gekocht je krijgt nu " + tc + " munten per dag. Je balans is: " + coins + " munten.")
              print("Wil je nog iets anders kopen ?")    
else:
    print("Je kan niks meer kopen. \n Kom morgen terug en krijg meer munten!")


