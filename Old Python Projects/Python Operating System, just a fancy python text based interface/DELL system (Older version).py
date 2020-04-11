#IMPORTS AND STARTING VALUES:
import time
import random
login_first_time = 1
username = 'i'
password = 'i'





#APPS:
def examrevise():
    find = input("what do you wanna find?")
    if find == "deconmposition":
        print("What is decomposition?")
        print("Decomposition is where you break complex issues or ideas into ever smaller tasks or segments.")
        print("Why is it important?")
        print("Well it allows you to focus on one thing at a time, you can more easily look at details.")
        print("Makes the solving of problems easier as well/")
        print("What is involved?")
        print("Ideintifying and describing the issues and the processes in general, breaks down the steps needed,")
        print("pattern recongition.")
        print("What is a pattern?")
        print("A set of characteristics in which is common between things.")
        print("Abstraction is the simplification of a more complex process or feature.")
        print("Generalisation is the process of ignoring a process or feature.")
        print("Reason for using it is becuase of you would not always want every detail into something or would not")
    else:
        print("invalid, please try again or write leave to go back to main menu")
        #Please continue this from classroom



#CORE CODE:
def load():
    time.sleep(0.1)
    print("      ///////////////////////////////////")
    time.sleep(0.1)
    print("     /  /////  /////  /      /   (x86) /")
    time.sleep(0.1)
    print("    /  /   /  /      /      /         /")
    time.sleep(0.1)
    print("   /  /   /  /////  /      /         /")
    time.sleep(0.1)
    print("  /  /   /  /      /      /         /")
    time.sleep(0.1)
    print(" /  /////  /////  /////  /////     /")
    time.sleep(0.1)
    print("///////////////////////////////////")
    time.sleep(0.1)
    print("READING HDD...")
    time.sleep(1)
    print("LOADING...")
    time.sleep(1)
    print("LOADING...")
    time.sleep(1)
    print("LOADING...")
    login(username,password,login_first_time)

def login(username,password,login_first_time):
    if login_first_time == 1:
        print("Welcome to the first time using DELL x86, please enter a username and password for future use")
        username = input("Username:")
        password = input("Password:")
        login_first_time = 0
    else:
        correct = 0
        tries = 0
        while correct == 0:
            print("Please enter your login")
            loginusername = input("Username:")
            loginpassword = input("Password:")
            if loginusername == username and loginpassword == password:
                correct = 1
                print("Logged in successfully!")
            else:
                tryuses = 0
                tries = tries + 1
                triesleft = 5 - tries
                if triesleft == 0:
                    tryuses = tryuses + 1
                    timelocked = tryuses * 600
                    print("You will be locked for:",timelocked," seconds.")
                    time.sleep(timelocked)
                    tries = 0
                    print("You may try again. If you fails you will be locked for 2 times longer.")
                else:
                    print("Password or username is incorrect, please try again, tries left:", triesleft)
    menu()
def menu():
    quits = 0
    while quits == 0:
        print("Welcome, please enter a command. If you are not aware of any commands please enter help for assistance")
        command = input("/")
        if command == "help":
            print("here is the current list of commands: help, lock,")
        elif command == "lock":
            login(username,password,0)
        elif command == "exam revision":
            examrevise()

load()
menu()
