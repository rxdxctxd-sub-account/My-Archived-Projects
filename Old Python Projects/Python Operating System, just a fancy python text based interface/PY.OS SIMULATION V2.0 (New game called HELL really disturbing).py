import random
import time
import sys
import os
from random import randint
global password
global data
global check1
global eXit
global exe
data = 0
password = ""
check1 = 0
eXit = 0
exe = 0
gamedata = 0
gamesavename = ""
def hell(gamedata,gamesavename):
    print("before you enter please respect the gamesave feature is not entirely working and will be fixed in PATCH 3.0")
    time.sleep(1)
    print("      ////////////////////////////////////////")
    print("     / /    /   /////    /        /         /")
    print("    / /    /   /        /        /         /")
    print("   / //////   /////    /        /         /")
    print("  / /    /   /        /        /         /")
    print(" / /    /   //////   //////   //////    /")
    print("////////////////////////////////////////")
    print("PUNY MAN ENTER IF YOU DARE! (PRESS ENTER TO START)")
    input("")
    time.sleep(1)
    print("")
    print("CHEACKING FOR GAME SAVE DATA...")
    time.sleep(1)
    print("")
    print("CHEACKING FOR  GAME SAVE DATA...")
    time.sleep(1)
    print("")
    print("CHEACKING FOR GAME SAVE DATA...")
    while gamedataload == 0:
        if gamedata == 0:
            print("PICK NAME HELLISH FIEND!")
            gamesavename = input("")
            return gamesavename
            time.sleep(1)
            print("")
            print("YOU SURE DISGUSTING HUMAN? (Y/N)")
            lax = input("")
            lax = lax.lower()
            if lax = "y":
                gamedataload = 1
            else:
                gamedataload = 0    
        else:
            print("GREETINGS,",gamesavename)
    time.sleep(1)
    print("")
    print("BOOTING...")
    time.sleep(1)
    print("")
    print("BOOTING...")
    time.sleep(1)
    print("")
    print("BOOTING...")
    time.sleep(1)
    print("")
    print("BOOTIED!")
    time.sleep(1)
    print("")
    print("A disturbed, demonic creature lies ahead of you, it cannot yet sense your presence...")
    time.sleep(5)
    print("")
    print("Blood... Your gut feels nice and warm as it oozes hot, succulent blood, you start to feel dizzy and lose feeling in the legs.You could wrap some cloth around the wound, would you like to do this? (Y/N)")
    q = input("")
    q = q.lower()
    if q == "y":
        time.sleep(1)
        print("")
        print("The rough cloth feels so good but the you thirst for blood grows...")
        time.sleep(3)
        print("")
        print("You see an obscure weapon to the left, maybe it could make the hound sleep... pick it up?")
        q = input("")
        q = q.lower()
        if q == "y":
            time.sleep(1)
            print("")
            print("you penetrate the hole on the back of the weapon, you feel a trigger with rusty spikes that softly blanket your fleshless fingers. You rip your teeth out and put it into the dish and slap the frozen but burnt disc into the weapon")
            time.sleep(6)
            print("")
            print("Instantly you feel a scratch on your back, you turn to pet the hound and you...")
            hell()
        else q == "n":
            time.sleep(1)
            print("")
            print("You decide to wait and pick your scabs for the tender meat that wait.")
    else:
        time.sleep(1)
        print("")
        print("'mmmmmmm', your guts pour out, you touch them and feel the tender flesh that lurk inside your body. FINALLY FREE!")
        time.sleep(1)
        print("")
        print("you go for a lick to taste the juice then...")
        hell()





























def BOOT(data,password,check1):
    print("    ///////////////////////////////////////")
    print("   / PY.OS: STANDARD EDITION             /")
    print("  / VERSION 0.2 X86 AND ARM COMPATIBLE  /")
    print(" / BUILT WITH PYTHON (3.6 WINDOWS X86) /")
    print("///////////////////////////////////////")
    print("")
    time.sleep(1)
    print("")
    time.sleep(1)
    print("PY.OS IS STARTING, PLEASE DO NOT TURN OFF WHILE THE OS IS LOADING...")
    print("")
    time.sleep(1)
    print("LOADING....")
    print("")
    time.sleep(1)
    print("LOADING....")
    print("")
    time.sleep(1)
    print("LOADING....")
    print("")
    time.sleep(1)
    print("LOADING....")
    print("")
    time.sleep(1)
    print("LOADING....")
    print("")
    time.sleep(1)
    print("BOOTED!")
    print("")
    time.sleep(1)
    if data == 0:
        print("ADD PASSWORD:")
        password = input("")
        data = 1
        time.sleep(1)
        print("WELCOME USER TO PY.OS PLEASE ENJOY, USE !HELP FOR COMMANDS")
        mainmen(data,password,check1,exe)
        time.sleep(1)
        print("")
    else:
        while check1 == 0:
            print("LOGIN:")
            login = input("")
            time.sleep(1)
            if login != password:
                print("ERROR: INCORRECT LOGIN, TRY AGAIN..")
            else:
                print("SUCCESS: WELCOME BACK USER, USE !HELP FOR HELP WITH ALL COMMANDS")
                check1 = 1
                mainmen(data,password,check1,exe)
                time.sleep(1)
                print("")
    return data
    return password
def mainmen(data,password,check1,exe):
    while exe == 0:
        INPUT = input("")
        INPUT = INPUT.lower()
        time.sleep(1)
        print("WAIT...")
        time.sleep(1)
        if INPUT == ("!time"):
            localtime = time.asctime( time.localtime(time.time()) )
            print("TIME IS:",localtime)
        elif INPUT == "!help":
            print("COMMANDS: !help, !time, !calculator, !book, !exit, !games, !clear")
        elif INPUT == "!games":
            print("GAMES: !HELL, !GUESSING GAME")
            play = input("")
            play.lower()
            if play == ("!hell"):
                hell()
        elif INPUT == "!calculator":
            main()
        elif INPUT == "!book":
            print("NO BOOKS INSTALLED")
        elif INPUT == "!clear":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
        elif INPUT == "!exit":
            print("YOU MAY TURN OFF PC!")
            exe = 1
        elif INPUT == "!LIAMLIAM":
            print("SECRETS LOADING...")
            time.sleep(1)
            print("HAHAHAHAHAHAHAHAHAH!")
            time.sleep(1)
            print("IM NORMAL!, THAT IS MY SECRET.")
        else:
            print("ERROR: INVALID COMMAND, USE !HELP FOR COMMANDS")



def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1/num2

def multi(num1,num2):
    return num1*num2
def main():
    print("PICK AN OPTION: +, -, *, or /")
    operation = input("")
    time.sleep(1)
    print("")
    if (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print("OPTION INVALID.")
        time.sleep(1)
        print("")
        main()
    else:
        print("ENTER NUM1:")
        num1 = float(input(""))
        time.sleep(1)
        print("")
        print("ENTER NUM1=2:")
        num2 = float(input(""))
        time.sleep(1)
        print("")
        if (operation == "+"):
            print(add(num1, num2))
            time.sleep(1)
            print("")
            print("WOULD YOU LIKE TO DO ANOTHER CALCULATION? Y/N")
            opcalc = input("")
            time.sleep(1)
            print("")
            opcalc = opcalc.upper()
            if opcalc == "Y":
                main()
            else:
                print("RETURNING TO MAIN OS...")
                time.sleep(1)
                print("")
                BOOT(data,password,check1)
        elif (operation == "-"):
            print(subtract(num1, num2))
            print("")
            print("WOULD YOU LIKE TO DO ANOTHER CALCULATION? Y/N")
            opcalc = input("")
            time.sleep(1)
            print("")
            opcalc = opcalc.upper()
            if opcalc == "Y":
                main()
            else:
                print("RETURNING TO MAIN OS...")
                time.sleep(1)
                print("")
                BOOT(data,password,check1)
        elif (operation == "*"):
            print(multi(num1,num2))
            print("")
            print("WOULD YOU LIKE TO DO ANOTHER CALCULATION? Y/N")
            opcalc = input("")
            time.sleep(1)
            print("")
            opcalc = opcalc.upper()
            if opcalc == "Y":
                main()
            else:
                print("RETURNING TO MAIN OS...")
                time.sleep(1)
                print("")
                BOOT(data,password,check1)
        elif (operation == "/"):
            print(div(num1,num2))
            print("")
            print("WOULD YOU LIKE TO DO ANOTHER CALCULATION? Y/N")
            opcalc = input("")
            time.sleep(1)
            print("")
            opcalc = opcalc.upper()
            if opcalc == "Y":
                main()
            else:
                print("RETURNING TO MAIN OS...")
                time.sleep(1)
                print("")
                BOOT(data,password,check1)
print("Before we start your simulator of a python code based OS this is not the real deal and it is in the working. (wait 10 seconds after this message for PY.OS to begin)")
print("if you pick an invalid option 2 of things may happen. 1. it may restart question or 2. it may just contine with one option (usually defualt being no).")
time.sleep(10)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
BOOT(data,password,check1)       
    

