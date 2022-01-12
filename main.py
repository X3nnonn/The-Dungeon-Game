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
print2(col.WHITE + "Welcome, to begin enter the Difficulty that you want. (easy) 1-3 (hard)")
difficulty=int(input(" >>"))

while True:
  if difficulty == 1:
    dh=1
    ddmg=1
    dc=1.5
    dcr=random.randint(1,5)
    db=0.8
    dbr=random.randint(1,5)
    deh=1
    dedmg=1
    dec=1.5
    decr=random.randint(1,5)
    deb=0.8
    debr=random.randint(1,5)
    break
  elif difficulty == 2:
    dh=1
    ddmg=1.1
    dc=1.3
    dcr=random.randint(1,8)
    db=0.85
    dbr=random.randint(1,8)
    deh=1.2
    dedmg=1.1
    dec=1.4
    decr=random.randint(1,5)
    deb=0.8
    debr=random.randint(1,5)
    break
  elif difficulty == 3:
    dh=1.2
    ddmg=1.3
    dc=1.5
    dcr=random.randint(1,10)
    db=0.8
    dbr=random.randint(1,10)
    deh=1.3
    dedmg=1.4
    dec=1.3
    decr=random.randint(1,4)
    deb=0.9
    debr=random.randint(1,4)
    break
  else:
    print2("That is not a valid Difficulty. Try Again.")
    difficulty=int(input(" >>"))

print2("\nAlright, let's begin!")

