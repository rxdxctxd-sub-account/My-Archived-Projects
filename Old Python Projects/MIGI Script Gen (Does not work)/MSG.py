#import os  
#needed becuase we will be making directories
import PySimpleGUI as sg


M = [  
        [sg.Text('Hello, welcome back to the MSG Project.')],           
        [sg.Text('Please pick either easy or advanced mode scripting:')],
        [sg.InputOptionMenu(('Advanced', 'Easy'))],
        [sg.Submit('next'), sg.Quit('Quit')]
       ]
H = [
        [sg.Text('Do you want a mod template?'),sg.InputOptionMenu(('No','Yes'))],
        [sg.Text("")],
        [sg.Text('What is the name of your weapon?'),sg.InputText('')], 
        [sg.Text('Does your weapon have any special attributes?'),sg.InputOptionMenu(('No', 'Revolver','Burst Fire','Scoped','silenced','forced silenced'))],
        [sg.Text("If there is an special attribute you will be able to edit its data later on.")],
        [sg.Text("Availabile for?"),sg.InputOptionMenu(('all','CT','T'))],
        [sg.Text("")],
        [sg.Text("DPS stats:")],
        [sg.Text("Raw damage?"),sg.Slider(range=(1, 500), orientation='h', size=(100, 10), default_value=25)],
        [sg.Text("Armor penetration? (Ratio)"),sg.InputText('')],
        [sg.Text("Object penetration?"),sg.InputText('')],
        [sg.Text("Firerate? (RPM)"),sg.Slider(range=(1, 1500), orientation='h', size=(250, 10), default_value=1)],
        [sg.Text("Automatic?"),sg.OptionMenu(('1','0'))],
        [sg.Text("Bullet Multiplier? (Used for shotguns)"),sg.Slider(range=(1, 30), orientation='h', size=(100, 10), default_value=1)],
        [sg.Text("")],
        [sg.Text("Inaccuracy stats:")],
        [sg.Text("Crouching?"),sg.InputText('')],
        [sg.Text("Standing?"),sg.InputText('')],
        [sg.Text("Moving?"),sg.InputText('')],
        [sg.Text("Jumping?"),sg.InputText('')],
        [sg.Text("Ladder?"),sg.InputText('')],
        [sg.Text("Spread?"),sg.InputText('')],
        
        [sg.Text("")],
        [sg.Submit('next')]
     ]
H2 = [
        [sg.Text("Recoil:")],
        [sg.Text("Pattern Seed?"),sg.InputText('')],
        [sg.Text("Angle?")],
        [sg.Text("Angle Variance?"),sg.InputText('')],
        [sg.Text("Magnitude?"),sg.InputText('')],
        [sg.Text("Magnitude Variance?"),sg.InputText('')],
        [sg.Text("")],
        [sg.Text("Ammo")],
        [sg.Text("Reserve?"),sg.InputText('')],
        [sg.Text("Primary?"),sg.InputText('')],
        [sg.Text("")],
        [sg.Text("Range:")],
        [sg.Text("Max range?"),sg.InputText('')],
        [sg.Text("Range modifier?"),sg.InputText('')],
        [sg.Text("")],
        [sg.Text("Misc:")],
        [sg.Text("Max player speed?"),sg.InputText('')],
        [sg.Text("Crosshair min distance?"),sg.InputText('')],
        [sg.Text("Weapon Weight?"),sg.InputText('')],
        [sg.Text("Flinch velocity (large)?"),sg.InputText('')],
        [sg.Text("Flinch velocity (small)?"),sg.InputText('')],
        [sg.Text("recovery time crouch?"),sg.InputText('')],
        [sg.Text("recovery time stand?"),sg.InputText('')],
        [sg.Text("recovery time crouch final?"),sg.InputText('')],
        [sg.Text("recovery time stand final?"),sg.InputText('')],
        [sg.Text("rumble effect?"),sg.InputText('')],
        [sg.Text("tracer frequency?"),sg.InputText('')],
        [sg.Text("addon scale?"),sg.InputText('')],
        [sg.Text("heat per shot?"),sg.InputText('')],

        [sg.Submit('next')]
      ]
HA = [
        [sg.Text("Here you can mod the alt stats.")],
        [sg.Text("")],
        [sg.Text("Recoil:")],
        [sg.Text("Angle alt?"),sg.InputText('')],
        [sg.Text("Angle Variance alt?"),sg.InputText('')],
        [sg.Text("Magnitude alt?"),sg.InputText('')],
        [sg.Text("Magnitude Variance alt?"),sg.InputText('')],
        [sg.Text("")],
        [sg.Text("Inaccuracy stats:")],
        [sg.Text("Crouching alt?"),sg.InputText('')],
        [sg.Text("Standing alt?"),sg.InputText('')],
        [sg.Text("Moving alt?"),sg.InputText('')],
        [sg.Text("Jumping alt?"),sg.InputText('')],
        [sg.Text("Ladder alt?"),sg.InputText('')],
        [sg.Text("Spread alt?"),sg.InputText('')],
        [sg.Text("")],
        [sg.Text("DPS:")],
        [sg.Text("Firerate alt?"),sg.InputText('')],
        [sg.Text("")],
        [sg.Submit('next')]
      ]

HT = [
      [sg.Text('What file type is your mod?'),sg.InputOptionMenu(('p_', 'm_'))],
      [sg.Text('What ?'),sg.InputOptionMenu(('p_', 'm_'))],
      [sg.Text("")],
      [sg.Submit('next')]
      ]

#Variable to determine if user wants to exit.

#Menu, Sends user here until he is finished and he wants to 'Exit application'


def Menu():
    #Asks user to pick an option
    window = sg.Window('MSG Menu').Layout(M)
    stay,choice = window.Read()
    Exit = stay[0]
    choice = choice[0]
    window.Close()
    print(Exit)
    print(choice)
    if Exit == "Q":
        quit
    else:
        Main(choice)
 
def Main(choice):
    if choice == "Easy": 
        print("WIP, come back another time..")
    elif choice == "Advanced":
        print("gay")
        window = sg.Window('MSG Advanced').Layout(H)
        Next,attribute = window.Read()
        
        template = attribute[0]
        print(template)
        
        name = attribute[1]
        print(name)
        
        specialattribute = attribute[2]
        print(specialattribute)
        
        CTT = attribute[3]
        print(CTT)
        
        RD = attribute[4]
        print(RD)
        
        AP = attribute[5]
        print(AP)
        
        OP = attribute[6]
        print(OP)
        
        RPM = attribute[7]
        print(RPM)
        
        AUT = attribute[8]
        print(AUT)
        
        BM = attribute[9]
        print(BM)
        
        CA = attribute[10]
        print(CA)
        
        SA = attribute[11]
        print(SA)
        
        MA = attribute[12]
        print(MA)
        
        JA = attribute[13]
        print(JA)
        
        LA = attribute[14]
        print(LA)
        
        SPR = attribute[15]
        print(SPR)
        
        window.Close()
        
        window = sg.Window('MSG Advanced p2').Layout(H2)
        Next,attribute = window.Read()
        
        PS = attribute[0]
        print(PS)
        
        A = attribute[1]
        print(A)
        
        AV = attribute[2]
        print(AV)
        
        M = attribute[3]
        print(M)
        
        MV = attribute[4]
        print(MV)
        
        window.Close()
    else:
        print("Please try again... Invalid option.")    
    Menu()
Menu()






#DEVLOG:
#Started work on the GUI, needs the attributes that give model, class name and slot it replaces done but that can be done soon.
#The structure needs to be built and worked on heavily.