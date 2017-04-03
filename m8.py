from random import choice
from time import sleep
import time

print("Type de vraag in")
quest = input()
aws = str(quest)
aws = len(aws)
if aws < 5:
    print("Misschien")
elif aws < 15:
    print("Zeker wel")
elif aws > 20:
    print("Hou je bek. Gebeurt toch niet")
