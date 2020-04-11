
#from pip._internal import main as pipmain
#pipmain(['install', '--user', '--ignore-installed', 'pygame', 'arcade', 'PySimpleGUI'])

#////////////////////////////////////////////////////////////////////     
#THIS IS THE IMPORTS PORTION (DO NOT IMPORT AFTER THIS POINT)
#////////////////////////////////////////////////////////////////////
import PySimpleGUI as sg
import pandas as pd


#////////////////////////////////////////////////////////////////////     
#THIS IS THE INITAL VALUES PORTION
#////////////////////////////////////////////////////////////////////
#PN = player name (individual)
pn1 = "NaN"
pn2 = "NaN"
pn3 = "NaN"
pn4 = "NaN"
pn5 = "NaN"
pn6 = "NaN"
pn7 = "NaN"
pn8 = "NaN"
pn9 = "NaN"
pn10 = "NaN"
pn11 = "NaN"
pn12 = "NaN"
pn13 = "NaN"
pn14 = "NaN"
pn15 = "NaN"
pn16 = "NaN"
pn17 = "NaN"
pn18 = "NaN"
pn19 = "NaN"
pn20 = "NaN"


#PN = team name (team)
tn1 = "NaN"
tn2 = "NaN"
tn3 = "NaN"
tn4 = "NaN"
tn5 = "NaN"
tname = "NaN"
#////////////////////////////////////////////////////////////////////     
#THIS IS THE lAYOUT SECTION
#////////////////////////////////////////////////////////////////////

#GUI LAYOUT FOR MENU
M = [  
        [sg.Text('Hello, welcome back to the College Tournament database.')],           
        [sg.Text('Please Choose what side you would like to go to:')],
        [sg.InputOptionMenu(('Team', 'Individual'))],
        [sg.Submit('next'), sg.Quit('Quit')]
       ]
#GUI LAYOUT FOR SUB-MENU FOR INDIVIDUALS
SMI = [
        [sg.Text('Please Choose what side you would like to go to:')],
        [sg.InputOptionMenu(('Results Sheet', 'Results Input', 'Input','Looker'))],
        [sg.Submit('next'), sg.Quit('Back')]
       ]
#GUI LAYOUT FOR SUB-MENU FOR TEAMS
SMT = [
        [sg.Text('Please Choose what side you would like to go to:')],
        [sg.InputOptionMenu(('Results Sheet', 'Results Input', 'Input','Looker'))],
        [sg.Submit('next'), sg.Quit('Back')]
       ]
#GUI LAYOUT FOR TEAM LOOKER
TF = [  
        [sg.Text('Please find the team your looking for')],
        [sg.InputText('')],
        [sg.Submit('Next')]
       ]
#GUI LAYOUT FOR PLAYER LOOKER
IF = [  
        [sg.Text('Please find the player your looking for')],
        [sg.InputText('')],
        [sg.Submit('Next')]
       ]
#GUI LAYOUT FOR TEAM INPUTER
TI = [  
        [sg.Text('Please enter the new team name...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 1...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 2...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 3...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 4...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 5...')], 
        [sg.InputText('')],
        [sg.Submit('Return')]
       ]
#GUI LAYOUT FOR INDIVIDUAL INPUT
II = [
        [sg.Text('Please enter player...')],
        [sg.InputText('')],
        [sg.Submit('Return')]
        ]
#GUI LAYOUT FOR GAME RESULTS INPUT [team]
tn1 = ""
tn2 = ""
tn3 = ""
tn4 = ""
tn5 = ""
GRIT = [
        [sg.Text('Please enter the game played')],
        [sg.InputOptionMenu(('5 a side football', '400m relay', 'Team quiz','Escape room','Tower Challenge'))],
        [sg.Text('Please enter the rankings of team:'+tn1)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of team:'+tn2)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of team:'+tn3)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of team:'+tn4)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of team:'+tn5)],
        [sg.InputText('')],
        [sg.Submit('Return')]
       ]
#GUI LAYOUT FOR GAME RESULTS INPUT [individual]

GRII = [
        [sg.Text('Please enter the game played')],
        [sg.InputOptionMenu(('Basketball hoop challenge', '100m run', 'Individual quiz','Timed assault course','Individual Tower Challenge'))],
        [sg.Text('Please enter the rankings of player:'+pn1)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn2)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn3)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn4)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn5)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn6)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn7)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn8)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn9)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn10)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn11)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn12)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn13)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn14)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn15)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn16)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn17)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn18)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn19)],
        [sg.InputText('')],
        [sg.Text('Please enter the rankings of player:'+pn20)],
        [sg.InputText('')],
        [sg.Submit('Return')]
       ]
#GUI LAYOUT FOR INVALIDATION
IV = [  
        [sg.Text('This is invalid.. Please try again.')],           
        [sg.Submit('Ok')]
       ]
#GUI LAYOUT FOR TEAM INPUTER
TI = [  
        [sg.Text('Please enter a new team...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 1...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 2...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 3...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 4...')], 
        [sg.InputText('')],
        [sg.Text('Please enter player 5...')], 
        [sg.InputText('')],
        [sg.Submit('Return')]
       ]
#////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////     
#THIS IS THE FUNCTION PORTION
#////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////     
#BOOTS UP MENU
def run():
    #nextgui is used to determine where the program
    nextgui = ''
    #Runs the window from above called M
    window = sg.Window('Menu').Layout(M)
    stay,option = window.Read()
    option = option[0]
    print(option)
    window.Close()
    nextgui = stay[0]
    print(nextgui)
    if nextgui == 'n':
        runsubmenu(nextgui,option)
    else:
        quit
        


#Starts up the submenu of choice if it be the individual or team.
def runsubmenu(nextgui,option):
    #THIS IS THE TEAM HALF
    while nextgui == 'n':
        if option == 'Team':
            #Runs the window from above called
            window = sg.Window('Sub Menu Team').Layout(SMT)
            #opens the flat file in a csv format.
            df = pd.DataFrame.from_csv('team.txt',index_col= None)
            print(df)
            stay,option2 = window.Read()
            option2 = option2[0]
            window.Close()
            prev = 'T'
            #Makes sure when moving on to the next function it identifies the user wants the Team version of code.
            option1 = option2+prev
            print(option1)
            nextgui = stay[0]
            if nextgui == 'B':
                run()
            else:
                runfunctions(nextgui,option,option1,df)
                   
        #THIS IS THE INDIVIDUAL HALF
        elif option == 'Individual':
            #Runs the window from above called
            window = sg.Window('Sub Menu Individual').Layout(SMI)
            #opens the flat file in a csv format.
            df = pd.DataFrame.from_csv('individual.txt')
            print(df)
            stay,option2 = window.Read()
            option2 = option2[0]
            window.Close()
            prev = 'I'
            #Makes sure when moving on to the next function it identifies the user wants the Individual version of code.
            option1 = option2+prev
            print(option1)
            nextgui = stay[0]
            if nextgui == 'B':
                run()
            else:
                runfunctions(nextgui,option,option1,df)
        else:
            print("")
            runfunctions(nextgui,option,option1,df)



def runfunctions(nextgui,option,option1,df):
#////////////////////////////////////////////////////////////////////     
#THIS IS THE TEAM HALF
#////////////////////////////////////////////////////////////////////        
    #putting some inital values before letting users pick an option.
    if option1 == 'InputT':
        #Runs the window from above called
        window = sg.Window('Team Input').Layout(TI)
        stay, names = window.Read()
        nextgui = stay[0]
        print(nextgui)
        print(names)
        #tname = team name
        #pname = player name
        tname = names[0]
        pname1 = names[1]
        pname2 = names[2]
        pname3 = names[3]
        pname4 = names[4]
        pname5 = names[5]
        if tname == "":
            print("hoh")
        else:
            print(pname1)
            print(pname2)
            print(pname3)
            print(pname4)
            print(pname5)
            print(tname)
            #translates new team into a dataframe
            df2 = pd.DataFrame({"team":[tname],
                                "score":[0], 
                                "player1":[pname1],
                                "player2":[pname2],
                                "player3":[pname3],
                                "player4":[pname4],
                                "player5":[pname5],
                                })
            print(df2)
            #adds the new team's dataframe into the main dataframe
            df2.to_csv('team.txt',mode='a',header=False,index=False)
            print(df)
            #ADD PANDA CODE FOR EDITING HERE
        window.Close()
    elif option1 == 'Results InputT':
        df_copy = pd.concat([df['team'],df['score'],df['player1'],df['player2'],df['player3'],df['player4'],df['player5'],df['eventID'],df['position']], axis=1, keys=['team', 'score','player1','player2','player3','player4','player5','eventID','position'])
        print(df_copy)
        #Sorts
        df_copy.sort_values(['score'], ascending=[False], inplace = True)
        print(df_copy)
        df_copy.drop_duplicates(subset ="team", keep = 'first', inplace = True)
        print(df_copy)
        try:
            tn1 = df_copy.iloc[0,0]
            print(tn1)
        except:
            tn1 = "NaN"
            print("could not print tn1")
        try:
            tn2 = df_copy.iloc[1,0]
            print(tn2)
        except:
            tn2 = "NaN"
            print("could not print tn2")
        try:
            tn3 = df_copy.iloc[2,0]
            print(tn3)
        except:
            tn3 = "NaN"
            print("could not print tn3")
        try:
            tn4 = df_copy.iloc[3,0]
            print(tn4)
        except:
            tn4 = "NaN"
            print("could not print tn4")
        try:
            tn5 = df_copy.iloc[4,0]
            print(tn5)
        except:
            tn5 = "NaN"
            print("could not print tn5")
        
        GRIT =  [
                [sg.Text('Please enter the game played')],
                [sg.InputOptionMenu(('5 a side football', '400m relay', 'Team quiz','Escape room','Tower Challenge'))],
                [sg.Text('Please enter the rankings of team:'+tn1)],
                [sg.InputOptionMenu(('1','2','3','4','5'))],
                [sg.Text('Please enter the rankings of team:'+tn2)],
                [sg.InputOptionMenu(('1','2','3','4','5'))],
                [sg.Text('Please enter the rankings of team:'+tn3)],
                [sg.InputOptionMenu(('1','2','3','4','5'))],
                [sg.Text('Please enter the rankings of team:'+tn4)],
                [sg.InputOptionMenu(('1','2','3','4','5'))],
                [sg.Text('Please enter the rankings of team:'+tn5)],
                [sg.InputOptionMenu(('1','2','3','4','5'))],
                [sg.Submit('Return')]
                ]
        window = sg.Window('Results Inputter').Layout(GRIT)
        stay = window.Read()
        window.Close()
    #This is used to see overall rankings.   
    elif option1 == 'Results SheetT':
        df.copy(deep=True)
        #Makes copy of dataframe
        df_copy = pd.concat([df['team'],df['score'],df['player1'],df['player2'],df['player3'],df['player4'],df['player5'],df['eventID'],df['position']], axis=1, keys=['team', 'score','player1','player2','player3','player4','player5','eventID','position'])
        print(df_copy)
        #Sorts
        df_copy.sort_values(['score'], ascending=[False], inplace = True)
        print(df_copy)
        df_copy.drop_duplicates(subset ="team", keep = 'first', inplace = True)
        print(df_copy)
        try:
            tn1 = df_copy.iloc[0,0]
            print(tn1)
        except:
            tn1 = "NaN"
            print("could not print tn1")
        try:
            tn2 = df_copy.iloc[1,0]
            print(tn2)
        except:
            tn2 = "NaN"
            print("could not print tn2")
        try:
            tn3 = df_copy.iloc[2,0]
            print(tn3)
        except:
            tn3 = "NaN"
            print("could not print tn3")
        try:
            tn4 = df_copy.iloc[3,0]
            print(tn4)
        except:
            tn4 = "NaN"
            print("could not print tn4")
        try:
            tn5 = df_copy.iloc[4,0]
            print(tn5)
        except:
            tn5 = "NaN"
            print("could not print tn5")
        #GUI LAYOUT FOR RESULTS SHEET
        TRS = [  
                [sg.Text('This is the current Leaderboard:')],
                [sg.Text('Rank 1: '+tn1)], 
                [sg.Text('Rank 2: '+tn2)], 
                [sg.Text('Rank 3: '+tn3)], 
                [sg.Text('Rank 4: '+tn4)], 
                [sg.Text('Rank 5: '+tn5)], 
                [sg.Submit('Return')]
                ]
        window = sg.Window('Results Sheet').Layout(TRS)
        stay = window.Read()
        window.Close()
    elif option1 == 'LookerT':
        #Runs the window from above called
        window = sg.Window('Team Looker').Layout(TF)
        stay,lookingfor = window.Read()
        window.Close()
        lookingfor = lookingfor[0]
        tname = str(lookingfor)
        #making a mini set of data out of the main datbase to serve the purpose of finding the team and players.
        df2 = pd.concat([df['team'],df['player1'],df['player2'],df['player3'],df['player4'],df['player5']], axis=1, keys=['team', 'player1','player2','player3','player4','player5'])
        #making another mini set of data out of the main datbase to serve the purpose of finding the team and their positioning in events.
        df3 = pd.concat([df['team'],df['eventID'],df['position']], axis=1, keys=['team','eventID','position'])
        #used to search in the mini set of data for the specific team.
        locate = df2.loc[df2['team'] == tname]
        #used again to search in the other mini set of data for the specific team.
        locate2 = df3.loc[df3['team'] == tname]
        #sorting the data by the event.
        locate2.sort_values(['eventID'], ascending=[True], inplace = True)
        print(locate2)
        #trying to locate the player names
        try:
            pn1 = locate.iloc[0,1]
        except:
            pn1 = ''
        try:
            pn2 = locate.iloc[0,2]
        except:
            pn2 = ''
        try:
            pn3 = locate.iloc[0,3]
        except:
            pn3 = ''
        try:
            pn4 = locate.iloc[0,4]
        except:
            pn4 = ''
        try:
            pn5 = locate.iloc[0,5]
        except:
            pn5 = ''
        #making sure player names if they weer just numbers are turned into strings
        pn1 = str(pn1)
        pn2 = str(pn2)
        pn3 = str(pn3)
        pn4 = str(pn4)
        pn5 = str(pn5)
        #tryig to lcoate the events.
        try:
            en1 = locate2.iloc[0,2]
        except:
            en1 = ''
        try:
            en2 = locate2.iloc[1,2]
        except:
            en2 = ''
        try:
            en3 = locate2.iloc[2,2]
        except:
            en3 = ''
        try:
            en4 = locate2.iloc[3,2]
        except:
            en4 = ''
        try:
            en5 = locate2.iloc[4,2]
        except:
            en5 = ''
        #turns event scores into a string as pandas automatically makes it an interger.
        en1 = str(en1)
        en2 = str(en2)
        en3 = str(en3)
        en4 = str(en4)
        en5 = str(en5)
        
        if pn1 == "":
            #worked indicates if the team was found or not.
            worked = '0'
        else:
            worked = '1'
        if worked == '1':
            #GUI LAYOUT FOR FOUND TEAM
            TFO = [
                    [sg.Text('We found: '+tname)],
                    [sg.Text('player 1: '+pn1)],
                    [sg.Text('player 2: '+pn2)],
                    [sg.Text('player 3: '+pn3)],
                    [sg.Text('player 4: '+pn4)],
                    [sg.Text('player 5: '+pn5)],
                    [sg.Submit('Next')]
                    ]
            #opens to tell user that it had found the team and tell them the players in the team
            window = sg.Window('Team Found').Layout(TFO)
            stay = window.Read()
            window.Close()
            #GUI LAYOUT FOR FOUND TEAM EVENTS PLACEMENT
            TFO2 = [
                    [sg.Text('Positioning of: '+tname)],
                    [sg.Text('Football: '+en1)],
                    [sg.Text('Escape Room: '+en2)],
                    [sg.Text('400m Relay: '+en3)],
                    [sg.Text('Team Quiz: '+en4)],
                    [sg.Text('Tower Challenge: '+en5)],
                    [sg.Submit('Next')]
                    ]
            #opens to tell user about their rankings in the events they have attended.
            window = sg.Window('Team Found').Layout(TFO2)
            stay = window.Read()
            window.Close()
        else:
            #Runs a window to tell the user that the team was not found.
            window = sg.Window('There has been an issue').Layout(IV)
            window.Read()
            window.Close()
    else:
        runsubmenu(nextgui,option)
#////////////////////////////////////////////////////////////////////     
#THIS IS THE INDIVIDUAL HALF
#////////////////////////////////////////////////////////////////////
    #putting some inital values before letting users pick an option.
    if option1 == 'InputI':
        #Runs the window from above called
        window = sg.Window('Individual Input').Layout(II)
        stay, names = window.Read()
        nextgui = stay[0]
        print(nextgui)
        print(names)
        #iname = individual name
        iname = names[0]
        if iname == "":
            print("hoh")
        else:
            print(iname)
            #translates new player into a dataframe
            df2 = pd.DataFrame({"individual":[iname],
                                "score":[0], 
                                })
            print(df2)
            #adds the new player's dataframe into the main dataframe
            df2.to_csv('individual.txt',mode='a',header=False,index=False)
            print(df)
        window.Close()
        

    elif option1 == 'Results InputI':
        df_copy = pd.concat([df['individual'],df['score'],df['eventID'],df['position']], axis=1, keys=['individual','score','eventID','position'])
        print(df_copy)
        #Sorts
        df_copy.sort_values(['score'], ascending=[False], inplace = True)
        print(df_copy)
        df_copy.drop_duplicates(subset ="individual", keep = 'first', inplace = True)
        print(df_copy)
        try:
            pn1 = df_copy.iloc[0,0]
            pn1 = str(pn1)
            print(pn1)
        except:
            pn1 = "NaN"
            print("could not print tn1")
        try:
            pn2 = df_copy.iloc[1,0]
            pn2 = str(pn2)
            print(pn2)
        except:
            pn2 = "NaN"
            print("could not print tn2")
        try:
            pn3 = df_copy.iloc[2,0]
            pn3 = str(pn3)
            print(pn3)
        except:
            pn3 = "NaN"
            print("could not print tn3")
        try:
            pn4 = df_copy.iloc[3,0]
            pn4 = str(pn4)
            print(pn4)
        except:
            pn4 = "NaN"
            print("could not print tn4")
        try:
            pn5 = df_copy.iloc[4,0]
            pn5 = str(pn5)
            print(pn5)
        except:
            pn5 = "NaN"
            print("could not print tn5")
        try:
            pn6 = df_copy.iloc[5,0]
            pn6 = str(pn6)
            print(pn6)
        except:
            pn6 = "NaN"
            print("could not print tn5")
        try:
            pn7 = df_copy.iloc[7,0]
            pn7 = str(pn7)
            print(pn7)
        except:
            pn7 = "NaN"
            print("could not print tn5")
        try:
            pn8 = df_copy.iloc[8,0]
            pn8 = str(pn8)
            print(pn8)
        except:
            pn8 = "NaN"
            print("could not print tn5")
        try:
            pn9 = df_copy.iloc[9,0]
            pn9 = str(pn9)
            print(pn9)
        except:
            pn9 = "NaN"
            print("could not print tn5")
        try:
            pn10 = df_copy.iloc[10,0]
            pn10 = str(pn10)
            print(pn10)
        except:
            pn10 = "NaN"
            print("could not print tn5")
        try:
            pn11 = df_copy.iloc[11,0]
            pn11 = str(pn11)
            print(pn11)
        except:
            pn11 = "NaN"
            print("could not print tn5")
        try:
            pn12 = df_copy.iloc[12,0]
            pn12 = str(pn12)
            print(pn12)
        except:
            pn12 = "NaN"
            print("could not print tn5")
        try:
            pn13 = df_copy.iloc[13,0]
            pn13 = str(pn13)
            print(pn13)
        except:
            pn13 = "NaN"
            print("could not print tn5")
        try:
            pn14 = df_copy.iloc[10,0]
            pn14 = str(pn14)
            print(pn14)
        except:
            pn14 = "NaN"
            print("could not print tn5")
        try:
            pn15 = df_copy.iloc[10,0]
            pn15 = str(pn15)
            print(pn15)
        except:
            pn15 = "NaN"
            print("could not print tn5")
        try:
            pn16 = df_copy.iloc[16,0]
            pn16 = str(pn16)
            print(pn16)
        except:
            pn16 = "NaN"
            print("could not print tn5")
        try:
            pn17 = df_copy.iloc[17,0]
            pn17 = str(pn17)
            print(pn17)
        except:
            pn17 = "NaN"
            print("could not print tn5")
        try:
            pn18 = df_copy.iloc[18,0]
            pn18 = str(pn18)
            print(pn18)
        except:
            pn18 = "NaN"
            print("could not print tn5")
        try:
            pn19 = df_copy.iloc[19,0]
            pn19 = str(pn19)
            print(pn19)
        except:
            pn19 = "NaN"
            print("could not print tn5")
        try:
            pn20 = df_copy.iloc[20,0]
            pn20 = str(pn20)
            print(pn20)
        except:
            pn20 = "NaN"
            print("could not print tn5")
        GRII =  [
                [sg.Text('Please enter the game played')],
                [sg.InputOptionMenu(('Basketball hoop challenge', '100m run', 'Quiz','Timed assault course','Tower Challenge'))],
                [sg.Text('Please enter the rankings of player:'+pn1)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn2)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn3)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn4)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn5)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn6)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn7)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn8)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn9)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn10)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Submit('Return')]
                ]
        GRII2 = [
                [sg.Text('Part 2')],
                [sg.Text('Please enter the rankings of player:'+pn11)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn12)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn13)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn14)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn15)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn16)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn17)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn18)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn19)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Text('Please enter the rankings of player:'+pn20)],
                [sg.InputOptionMenu(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))],
                [sg.Submit('Return')]
                ]
        window = sg.Window('Results Inputter').Layout(GRII)
        stay,option = window.Read()
        print(option)
        print(stay)
        window.Close()
        window = sg.Window('Results Inputter').Layout(GRII2)
        stay,option = window.Read()
        print(option)
        print(stay)
        window.Close()
    #This is used to see overall rankings.   
    elif option1 == 'Results SheetI':
        df.copy(deep=True)
        #Makes copy of dataframe
        df_copy = pd.concat([df['individual'],df['score'],df['eventID'],df['position']], axis=1, keys=[ 'individual','score','eventID','position'])
        print(df_copy)
        #Sorts
        df_copy.sort_values(['score'], ascending=[False], inplace = True)
        print(df_copy)
        df_copy.drop_duplicates(subset ="individual", keep = 'first', inplace = True)
        print(df_copy)
        try:
            tn1 = df_copy.iloc[0,0]
            print(pn1)
        except:
            tn1 = "NaN"
            print("could not print pn1")
        try:
            tn2 = df_copy.iloc[1,0]
            print(tn2)
        except:
            tn2 = "NaN"
            print("could not print tn2")
        try:
            tn3 = df_copy.iloc[2,0]
            print(tn3)
        except:
            tn3 = "NaN"
            print("could not print tn3")
        try:
            tn4 = df_copy.iloc[3,0]
            print(tn4)
        except:
            tn4 = "NaN"
            print("could not print tn4")
        try:
            tn5 = df_copy.iloc[4,0]
            print(tn5)
        except:
            tn5 = "NaN"
            print("could not print tn5")
        #GUI LAYOUT FOR RESULTS SHEET
        TRS = [  
                [sg.Text('This is the current Leaderboard:')],
                [sg.Text('Rank 1: '+tn1)], 
                [sg.Text('Rank 2: '+tn2)], 
                [sg.Text('Rank 3: '+tn3)], 
                [sg.Text('Rank 4: '+tn4)], 
                [sg.Text('Rank 5: '+tn5)], 
                [sg.Submit('Return')]
                ]
        window = sg.Window('Results Sheet').Layout(TRS)
        stay = window.Read()
        window.Close()
    elif option1 == 'LookerI':
        #Runs the window from above called
        window = sg.Window('Player Looker').Layout(IF)
        stay,lookingfor = window.Read()
        window.Close()
        lookingfor = lookingfor[0]
        tname = str(lookingfor)
        #making a mini set of data out of the main datbase to serve the purpose of finding the team and players.
        df2 = pd.concat([df['individual'],df['score'],df['eventID'],df['position']], axis=1, keys=[ 'individual','score','eventID','position'])
        #making another mini set of data out of the main datbase to serve the purpose of finding the team and their positioning in events.
        df3 = pd.concat([df['individual'],df['score'],df['eventID'],df['position']], axis=1, keys=[ 'individual','score','eventID','position'])
        #used to search in the mini set of data for the specific team.
        locate = df2.loc[df2['individual'] == tname]
        #used again to search in the other mini set of data for the specific team.
        locate2 = df3.loc[df3['individual'] == tname]
        #sorting the data by the event.
        locate2.sort_values(['eventID'], ascending=[True], inplace = True)
        print(locate2)
        #trying to locate the player names
        try:
            in1 = locate.iloc[0,0]
            in1 = str(in1)
        except:
            in1 = 'NaN'
            print('NaN')
        #making sure player names if they weer just numbers are turned into strings
        #tryig to lcoate the events.
        try:
            en1 = locate2.iloc[0,2]
        except:
            en1 = ''
        try:
            en2 = locate2.iloc[1,2]
        except:
            en2 = ''
        try:
            en3 = locate2.iloc[2,2]
        except:
            en3 = ''
        try:
            en4 = locate2.iloc[3,2]
        except:
            en4 = ''
        try:
            en5 = locate2.iloc[4,2]
        except:
            en5 = ''
        #turns event scores into a string as pandas automatically makes it an interger.
        en1 = str(en1)
        en2 = str(en2)
        en3 = str(en3)
        en4 = str(en4)
        en5 = str(en5)
        
        if in1 == "":
            #worked indicates if the player was found or not.
            worked = '0'
        else:
            worked = '1'
        if worked == '1':
            #GUI LAYOUT FOR FOUND TEAM
            PFO = [
                    [sg.Text('We found: '+in1)],
                    [sg.Submit('Next')]
                    ]
            #opens to tell user that it had found the team and tell them the players in the team
            window = sg.Window('Player Found').Layout(PFO)
            stay = window.Read()
            window.Close()
            #GUI LAYOUT FOR FOUND TEAM EVENTS PLACEMENT
            PFO2 = [
                    [sg.Text('Positioning of: '+in1)],
                    [sg.Text('Basketball hoop challenge: '+en1)],
                    [sg.Text('100m Run: '+en2)],
                    [sg.Text('Individual quiz: '+en3)],
                    [sg.Text('Timed assault course: '+en4)],
                    [sg.Text('Tower Challenge: '+en5)],
                    [sg.Submit('Next')]
                    ]
            #opens to tell user about their rankings in the events they have attended.
            window = sg.Window('Player Found').Layout(PFO2)
            stay = window.Read()
            window.Close()
        else:
            #Runs a window to tell the user that the team was not found.
            window = sg.Window('There has been an issue').Layout(IV)
            window.Read()
            window.Close()
    else:
        runsubmenu(nextgui,option)      



run()
#EVENTS DICTONARY FOR TEAMS:
# 1 = FOOTBALL
# 2 = ESCAPEROOM
# 3 = RELAY
# 4 = QUIZ
# 5 = TOWER
#EVENTS DICTONARY FOR INDIVIDUAL:

