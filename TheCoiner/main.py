import time
import datetime
d = datetime.date.today()
dm = d.month
print ('Welkom bij TheCoiner')
file = 'data/month.txt'
f = open(file)
file_contents = f.read()
pdm = file_contents

with open("data/month.txt", "w") as out_coins:
           char = "1"
           for i in range(len(char)):
                out_string = str(dm)
                out_coins.write(out_string)

tc = str(1)                
                
if int(dm) > int(pdm):
    print('You got ' + tc + ' coin(s)')
    file = 'data/coins.txt'
    f = open(file)
    file_contents = f.read()
    coins = file_contents
    coins = int(coins) + 1
    coins = str(coins)
    
    with open("data/coins.txt", "w") as out_coins:
           char = "1"
           for i in range(len(char)):
                out_string = str(coins)
                out_coins.write(out_string)
                
    file = 'data/coins.txt'
    f = open(file)
    file_contents = f.read()
    coins = file_contents

    print('Je hebt ' + coins + ' munten')






    '''
    with open("regn.txt", "w") as out_regn:
           char = "1"
           for i in range(len(char)):
                out_string = str(regn)
                out_regn.write(out_string)
        
        regn = regn + 1	
        file = 'regn.txt'
        f = open(file)
        file_contents = f.read()
    '''
else :
     print("You didn't got any coin")
     file = 'data/coins.txt'
     f = open(file)
     file_contents = f.read()
     coins = file_contents
     coins = str(coins)
     print('Je hebt ' + coins + ' munten')
