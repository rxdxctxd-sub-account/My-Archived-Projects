import time
global gamedata
global gamesavename
gamedata = 0
gamesavename = ""

def hell(gamedata,gamesavename):
    gamedataload = 0
    print("before you enter please respect the gamesave feature is not entirely working and will be fixed in PATCH 3.0")
    time.sleep(1)
    print("      ////////////////////////////////////////")
    print("     / /    /   /////    /        /         /")
    print("    / /    /   /        /        /         /")
    print("   / //////   /////    /        /         /")
    print("  / /    /   /        /        /         /")
    print(" / /    /   //////   //////   //////    /")
    print("////////////////////////////////////////")
    print("PUNY MAN ENTER IF YOU DARE! (PRESS ENTER TO START) BETTER CALL MUM BEFORE YOU DIE!")
    number = input("")
    if number == "07753257831":
        time.sleep(1)
        print("")
        print("well you want to know what happened? you never was in hell you was in HOME and you enjoyed it, the pleasures")
    elif number == "HOME":
        time.sleep(1)
        print("")
        print("you want to know what home is? its the hospital for people like YOU :)")
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
            time.sleep(1)
            print("")
            print("YOU SURE DISGUSTING HUMAN? (Y/N)")
            lax = input("")
            lax = lax.lower()
            if lax == "y":
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
    print("BOOTED!")
    time.sleep(1)
    print("")
    print("A disturbed, demonic creature lies ahead of you, it cannot yet sense your presence...")
    time.sleep(5)
    print("")
    print("Blood... Your gut feels nice and warm as it oozes hot, succulent blood, you start to feel dizzy and lose feeling in the legs. You could wrap some cloth around the wound, would you like to do this? (Y/N)")
    q = input("")
    q = q.lower()
    if q == "y":
        time.sleep(1)
        print("")
        print("The rough cloth feels so good but your thirst for blood grows...")
        time.sleep(3)
        print("")
        print("You see an obscure weapon to the left, maybe it could make the hound sleep... pick it up? (Y/N)")
        q = input("")
        q = q.lower()
        if q == "y":
            time.sleep(1)
            print("")
            print("you jump up and grab the weapon then proceed to penetrate the hole on the back of the weapon with your hand, you feel a trigger with rusty spikes that softly blanket your fleshless fingers. You rip your teeth out and put it into the dish and slap the frozen but burnt disc into the weapon")
            time.sleep(6)
            print("")
            print("Instantly you feel a scratch on your back, you turn to pet the hound and you...")
            time.sleep(1)
            print("")
            print("YOU DIED, PLEASE REBOOT GAME TO RETRY")
            hell(gamedata,gamesavename)
        elif q == "jack":
            time.sleep(1)
            print("")
            print("You see jack, you greet him and he greets back, he asks where you got your wound and you have no responce")
            time.sleep(3)
            print("")
            print("He guides you back to your cell and calls 999 for an ambulance but you secretly enjoy the pain...")
        else:
            time.sleep(1)
            print("")
            print("You decide to wait and pick your scabs for the tender meat that wait for your approval.")
            time.sleep(3)
            print("")
            print("The satanic hound sprints towards another creature, you should probably stay. will you? (Y/N)")
            q = input("")
            q = q.lower()
            if q == "n":
                time.sleep(1)
                print("")
                print("You spring onto your curved legs and skip towards a door")
                time.sleep(3)
                print("")
                print("The hound rams you through it but gets its mauled, tasty felsh stuck to the door, the juice pours out, so tasty, 'mmmmmm' you want to suck it? (Y/N)")
                q = input("")
                q = q.lower()
                if q == "y":
                    time.sleep(1)
                    print("")
                    print("'AHHHHH', you been filled with the juice, but you feel a orgasmic, tingly, burning sensation going through your...")
                    time.sleep(1)
                    print("")
                    print("YOU DIED, PLEASE REBOOT GAME TO RETRY")
                    hell(gamedata,gamesavename)
                else:
                    time.sleep(1)
                    print("")
                    print("You turn back around to only be surrounded by soothing lava, walls made of mashed dried flesh and crunchy bone, like the attractive cakes your mum made for your birthday...")
                    time.sleep(4)
                    print("")
                    print("You see out in the distance a seductive, mature and fleshy mammal, you should probably not harm it, or will you pick up a obscure rifle next to you? (Y/N)")
                    q = input("")
                    q = q.lower()
                    if q == "y":
                        time.sleep(1)
                        print("")
                        print("you snatch the rifle off of the wall then proceed to penetrate the hole on the back of the rifle with your hand, you feel a trigger covered like a blanket in rust that softly scrape of the scraps of meat your almost fleshless fingers. You rip your teeth out and put it into the mag and slap the mag into the rifle")
                        time.sleep(6)
                        print("")
                        print("You lock your decomposed eyes on to the beast and 'BANG' you killed it, no regrets just one person asleep, just remember they only go asleep to wake in hell. NO ONE GOES TO HEAVEN... YOU THINK THEY CARE? (Y/N)")
                        q = input("")
                        q = q.lower()
                        if q == "n":
                            print(":) EXACATLY THE GODS DONT CARE, WHY DO YOU THINK YOUR HERE? KILL THEM AND AVENGE YOURSELF")
                            time.sleep(3)
                            print("")
                            print("ANENGE YOURSELF? (Y/N)")
                            q = input("")
                            q = q.lower()
                            if q == "y":
                                time.sleep(1)
                                print("")
                                print("You fought, you killed 10 other people that day: policemen, doctors and civillians... now your are not alive, now you really are in HELL...")
                            elif q == "call mum":
                                time.sleep(1)
                                print("")
                                print("You retreat to the phone and call your mum, she picks up niave to the situation... she asks you what you are doing, before you can mutter a word you feel a sharp pain in your stomach and fall to the floor...")
                            else:
                                time.sleep(1)
                                print("")
                                print("You gave yourself up, you killed 1 person that day: Jack Willson... now you are not alive, now you are in ....!")
                        else:
                            print(":( AFTER EVERYTHING WE BEEN THROUGH? YOU REALLY THINK THE MAN UP THERE GIVES A SINGLE SHIT? FUCK YOU")
                 
                    else:
                        time.sleep(1)
                        print("you have no choice but to run so you did, never to be seen again, you see your flesh grow back, your torn clothes reapear onto your tender weak skin, your bones return to normal shape but this isnt you, this isnt the man who belongs in hell, they finally care they finally want you.")
                        time.sleep(1)
                        print("")
                        print("you awake in a prison cell again and this time your wanted jsut remember 07753257831")
            else:
                time.sleep(1)
                print("")
                print("you are instantly mauled to death in a soothing and gentle manner, :) YOU ARE FINALLY FREE!")
                time.sleep(1)
                print("")
                print("YOU DIED, PLEASE REBOOT TO RETRY")
hell(gamedata,gamesavename)
