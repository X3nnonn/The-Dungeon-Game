import random
from random import randint as rint
import colorama 
from colorama import Fore as col
import time
import sys

def print1(text, delay=0.003):
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(delay)
  print()

def print2(text, delay=0.05):
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(delay)
  print()

def print3(text, delay=0.075):
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(delay)
  print()

def wait(nn):
  n=0
  while n!=nn:
    print("\n")
    time.sleep(0.05)
    n+=1

level=['''
██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ░░███╗░░
██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ░████║░░
██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██╔██║░░
██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ╚═╝██║░░
███████╗███████╗░░╚██╔╝░░███████╗███████╗  ███████╗
╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ╚══════╝
''', '''
██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██████╗░
██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ╚════██╗
██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ░░███╔═╝
██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ██╔══╝░░
███████╗███████╗░░╚██╔╝░░███████╗███████╗  ███████╗
╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ╚══════╝
''', '''
██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██████╗░
██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ╚════██╗
██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ░█████╔╝
██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ░╚═══██╗
███████╗███████╗░░╚██╔╝░░███████╗███████╗  ██████╔╝
╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░
''', '''
██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ░░██╗██╗
██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ░██╔╝██║
██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██╔╝░██║
██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ███████║
███████╗███████╗░░╚██╔╝░░███████╗███████╗  ╚════██║
╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ░░░░░╚═╝
''', '''
██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ███████╗
██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ██╔════╝
██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██████╗░
██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ╚════██╗
███████╗███████╗░░╚██╔╝░░███████╗███████╗  ██████╔╝
╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░
''']

game_name='''
████████╗██╗░░██╗███████╗
╚══██╔══╝██║░░██║██╔════╝
░░░██║░░░███████║█████╗░░
░░░██║░░░██╔══██║██╔══╝░░
░░░██║░░░██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║
██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║
██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║
██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║
╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚══╝

░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
'''




print1(col.GREEN + game_name + '\n')
print2(col.BLUE + "Welcome, to begin enter the Difficulty that you want. (easy) 1-3 (hard)")
difficulty=int(input(col.WHITE+" >>"))

while True:
  if difficulty == 1:
    dh=1
    ddmg=1
    c=1.5
    cr=rint(1,5)
    b=0.8
    br=rint(1,5)
    deh=1
    dedmg=1
    ec=1.5
    ecr=rint(1,5)
    eb=0.8
    ebr=rint(1,5)
    break
  elif difficulty == 2:
    dh=1
    ddmg=1.1
    c=1.3
    cr=rint(1,8)
    db=0.85
    br=rint(1,8)
    deh=1.2
    dedmg=1.1
    dec=1.4
    decr=rint(1,5)
    deb=0.8
    debr=rint(1,5)
    break
  elif difficulty == 3:
    dh=1.2
    ddmg=1.3
    dc=1.5
    dcr=rint(1,10)
    db=0.8
    dbr=rint(1,10)
    deh=1.3
    dedmg=1.4
    dec=1.3
    decr=rint(1,4)
    deb=0.9
    debr=rint(1,4)
    break
  else:
    print2(col.BLUE+"That is not a valid Difficulty. Try Again.")
    difficulty=int(input(" >>"))

h=20*dh
eh=20*deh

print2(col.BLUE+"\nAlright, let's begin!")

wait(1)

lvl=0

print2(col.BLUE+"You see a cave entrance in the distance.\n'I should go in there,' you think to yourslef.\n\nYou go to the entrance of the cave and you see a monster waiting inside\n\nDo you want to 'leave' everything behind and finish your adventure or 'fight' the monster?")

choice1=input(col.WHITE+" >>")

if choice1.lower()=='fight':
  print2(col.BLUE+"\nYou decide to stay and fight this monster.\nOnce you enter the cave you realize you do not have a weapon to fight with.\nYou look around and find a rusty sword on the ground and pick it up, alerting the monster\n\n'I guess there's no backing out now'\n\n")

  print1(col.RED + level[lvl])
  lvl+=1
  print(col.WHITE)
  while eh>0:
    print("Your health=",h)
    print("The monster's health=",eh)
    atk=input(col.WHITE+"\nTo attack press enter.")

    cr
    ecr
    dmg=5*ddmg
    edmg=2*dedmg

    if cr==3:
      dmg+=c

    if ecr==3:
      edmg+=ec
    h-=edmg
    eh-=dmg
    wait(0)
  eh=20
  h=20
  print3(col.BLUE+"You took a lot of damage from that fight.\nOnce you catch your breath you notice some gold coins, where the monster had died, and pick them up.\nYou look around some more and find a splitting path.\nAt the end of the left path there is a glowing yellow light and you head towards it.\nYou find yourself at a shop of somesorts and see another person.\nYou go up to them and ask him why he's here...\nAll he does is nod.\nYou look around the shop and find some food, you start eating it and the shop keeper notices it and makes a 'cha-ching' noise.\nYou don't think much of it because your health is back to 100% until you look in your pocket to get the coins... They're gone\nYou begin to realize that the shop keeper took them when he made the noise.\nYou go back down the path and go to the right path now.\nYou find yourself another monster.\n\nDo you want to 'leave' everything behind and finish your adventure or 'fight' the monster?")
  choice2=input(col.WHITE+" >>")
  if choice2.lower()=='fight':
    while eh>0:
      print("Your health=",h)
      print("The monster's health=",eh)
      atk=input(col.WHITE+"\nTo attack press enter.")
      cr
      ecr
      dmg=5*ddmg
      edmg=2*dedmg
      if cr==3:
        dmg+=c
      if ecr==3:
        edmg+=ec
      h-=edmg
      eh-=dmg
      wait(0)
  else:
    choice1=leave






