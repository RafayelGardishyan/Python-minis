from datetime import datetime
now = datetime.now()
sps = now.second % 3
print ("Input stone/paper/scissors")
user = input()
print ("Your input is:" + str(user))

if sps == 0 :
  pc = "stone"
elif sps == 1 :
  pc = "paper"
elif sps == 2 :
  pc = "scissors"

print ("Computer says :" + pc)

if user == pc:
        print("Tie!")
elif user == "stone":
        if pc == "paper":
            print("You lose!", pc, "covers", user)
        else:
            print("You win!", user, "smashes", pc)
elif user == "paper":
        if pc == "scissors":
            print("You lose!", pc, "cut", user)
        else:
            print("You win!", user, "covers", pc)
elif user == "scissors":
        if pc == "stone":
            print("You lose...", pc, "smashes", user)
        else:
            print("You win!", user, "cut", pc)
else:
        print("That's not a valid play. Check your spelling!") 

print ("Thanks for playing this game")
