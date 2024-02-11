from Yahtzeegamecode import Game, Player, EasyAI, EZBoard, HardAI
## UI code ##

import random, math, PySimpleGUI as psg, time, os, sys , re, sqlite3, statistics, tkinter, threading


# Terminal UI

class Terminal:
    


        # initialise game
        def __init__(self):

            self.game = Game()

            

        # run game
            
        def run(self):
            
            
            while True:
                # get number of players
                try:
                    self.playernum = int(input("Enter the number of players: "))
                    self.AIplayers = int(input("Enter the number of AI players: "))
                    break
                except ValueError:
                    print("Invalid number of players")
                    continue



            
                    

                
            # add players to game
            for player in range(self.playernum):
                self.game.players.append(Player())

            for player in self.game.players:
                player.name = input("Enter your name: ")
            
            # add AI players to game
            for player in range(self.AIplayers):
                self.game.players.append(EasyAI())

            # get player names
            
            # play game
            while self.game.roundnum < 13:
                self.tround()

            print('Game Over!')
            
            # end sequence
            for player in self.game.players:
                print(player.name + "'s score is: " + str(player.scorecard.count_score()))
            print('the winner is '+ self.game.get_winner().name + ' with a score of ' + str(self.game.get_winner().scorecard.count_score()))

            

        # get user input for rerolls

        ###############################
        # USE OF RECURSIVE VALIDATION #
        ###############################
                
        def __get_reroll_choice(self):
            try:
                reroll_list = (input("Enter the dice indexes you want to reroll, seperated by a comma: ")).split(',')
                if reroll_list == ['']:
                    return []
                for dice in reroll_list:
                    if int(dice) not in range(1, 6):
                        print("Invalid choice- must be between 1 and 5")
                        reroll_list = self.__get_reroll_choice()
            except ValueError or TypeError:
                print("Invalid choice")
                reroll_list = self.__get_reroll_choice()
            
            return reroll_list
            
        # get user input for category choice

        def __get_category_choice(self,player):
            try:
                choice = (int(input("Enter your choice: ")))
            
            # check if choice is valid
            except ValueError or TypeError:
                print("Invalid choice")
                choice = self.__get_category_choice(player)

            if choice not in range(1, 14):
                print("Invalid choice- must be between 1 and 13")
                choice = self.__get_category_choice(player)
            

            
            if player.get_scorecard().scorecard[player.scorecard.keylist[choice-1]] != None:
                print("Category already scored")
                choice = self.__get_category_choice(player)
            

            return choice  

        # play round
           
        def tround(self):

            self.game.roundnum += 1

            print("Round " + str(self.game.roundnum))
            for player in self.game.players:
                if isinstance(player, EasyAI) or isinstance(player, HardAI):
                    self.__ai_turn(player)
                else:
                    self.turn(player)

        # play user turn
                        
        def turn(self,player):

            
            print(player.name + "'s turn")
            self.game.dice.roll()
            print("Your dice are: " + str(self.game.dice.get_dice()))
            while self.game.rerolls < self.game.REROLLS:
                self.game.rerolls += 1
                self.game.dice.reroll(self.__get_reroll_choice())
                print("Your dice are: " + str(self.game.dice.get_dice()))
            self.game.rerolls = 0
            player.scorecard.show_scorecard()
            choice = self.__get_category_choice(player)
            player.scorecard.score_roll(self.game.dice, choice)
            player.scorecard.show_scorecard()

        # play AI turn
            
        def __ai_turn(self,player):
                
                print(player.name + "'s turn")
                self.game.dice.roll()
                print("Your dice are: " + str(self.game.dice.get_dice()))
                self.game.rerolls = 0
                player.scorecard.show_scorecard()
                player.play()
                player.scorecard.show_scorecard()




# GUI 
                
class GUI:

    #dice image initialisation
    
    
    #GUI initialisation
    def __init__(self):
        self.game = Game()
        self.__theme = "DarkGrey1"
        self.__rules = 'Rules.txt'
        self.__aidifficulty = 'Easy'
        self.EZboardopt = False
        self.dice_colours = ['white', 'purple']
        self.dice_images = {
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None
    }
        self.__dice_unpack('white')


    # unpack dice images from folder
        

    #########################
    # DIRECT FILE ACCESSING # 
    #########################
        
    def __dice_unpack(self, colour):
        dice_images_path = os.path.join(colour, '')
        dicepack = enumerate(sorted([filename for filename in os.listdir(colour)]))
        for index, dice in dicepack:
            self.dice_images[index+1] = os.path.join(dice_images_path, dice)
            
    #run game in GUI
            
    

    '''def YahtzeePopUp(self):
        psg.popup('Yahtzee', auto_close_duration=3, image='YahtzeeGIF.gif')'''

    def run(self):
        # set theme
        psg.theme(self.__theme)
        #self.YahtzeePopUp()
        
        # main menu
        layout = [[psg.Text("Welcome to Yahtzee!", font=("Helvetica", 25))],
                  [psg.T("")],
                  [psg.Button("Start new Game", size = (50, 5) )],
                  [psg.T("")],
                  [psg.Button("Leaderboard", size = (50, 5))], 
                  [psg.T("")],
                  [psg.Button("Rules", size = (50, 5))],
                    [psg.T("")],
                    [psg.Button("Settings", size = (50, 5))],
                    [psg.T("")],
                    [psg.Button("Exit", size = (25, 2))]
                  ]
                  
        window = psg.Window("Yahtzee", layout, size=(700, 700), element_justification='c', resizable=True)
        window.finalize()
        window.maximize()

        while True: # fix later
            event, values = window.read()
            
            

            if event == "Start new Game":
                window.close()
                self.newgame()
                
                
            elif event == "Load Game":
                self.loadgame()
            
            elif event == "Leaderboard":
                self.leaderboard()
            
            elif event == "Rules":
                self.rules()

            elif event == "Settings":
                self.settings()
                window.close()
                psg.popup("Settings applied")
                self.run()

            elif event == "Exit":
                break
            
            elif event == psg.WIN_CLOSED:
                break
        
        window.close()

    # load leaderoard from database, display in table
        
    def leaderboard(self):
        
        # check if leaderboard exists
        if not os.path.isfile('leaderboard.db'):
            psg.popup("No leaderboard found")
            return
        
        # get leaderboard from database
        conn = sqlite3.connect('leaderboard.db')
        c = conn.cursor()
        c.execute("SELECT player_name, score FROM leaderboard ORDER BY score DESC")
        leaderboard = c.fetchall()
        conn.close()

        layout = [[psg.Text("Leaderboard")],
                  [psg.T("")],
                  [psg.Table(values = leaderboard, headings = ["Player", "Score"], num_rows=(len(leaderboard)), auto_size_columns=True, justification='c')],
                  [psg.Button("Back", size = (25, 2))]
                  ]
        window = psg.Window("Leaderboard", layout, element_justification='c')
        
        while True:
            event, values = window.read()
            if event == "Back":
                break
            
            elif event == psg.WIN_CLOSED:
                break
        
        window.close()

    # add player to leaderboard database
    def addtoleaderboard(self, player):
        # 
        conn = sqlite3.connect('leaderboard.db')
        c = conn.cursor()
        c.execute('''
                  CREATE TABLE IF NOT EXISTS leaderboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player_name TEXT,
                    score INTEGER
                    )
                    ''')

        c.execute("INSERT INTO leaderboard (player_name, score) VALUES (?, ?)", (player.name, player.scorecard.get_score()))
        conn.commit()
        conn.close()


    # rules page
    def rules(self):
        
        # read rules from file
        with open(self.__rules, 'r') as f:
            rules = f.read()

        layout = [[psg.Column([[psg.Text(rules)]], scrollable=True, vertical_scroll_only=True, size=(1100, 500))],
                 [psg.Button("Back", size = (25, 2))],
                 ]   
                    
                  
        window = psg.Window("Yahtzee rules", layout, element_justification='c', resizable=True, modal=True)

        while True:
            event, values = window.read()
            if event == "Back":
                break
                
            elif event == psg.WIN_CLOSED:
                break
        
        window.close()

    
    # starts a new game      
    def newgame(self):

        self.game = Game()


        while True:
            # get number of players
            try:
                self.playernum = psg.popup_get_text("Enter the number of players: ", modal = True)

                if self.playernum == None:
                    return self.run()
                else:
                    self.playernum = int(self.playernum)

                self.AIplayers = psg.popup_get_text("Enter the number of AI players: ")
                if self.AIplayers == None:
                    return self.run()
                else:
                    self.AIplayers = int(self.AIplayers)

                if self.playernum < 1 or self.AIplayers < 0 or self.AIplayers > 5:
                    #psg.popup('Invalid number of players')
                    raise ValueError
                else:
                    break
            except (ValueError, TypeError):
                psg.popup("Invalid number of players: must be at least 1 human player and no more than 5 AI players")
                continue
        
        ###########################
        # DYNAMIC OBJECT CREATION #
        ###########################
            
        for self.player in range(self.playernum):
            self.game.players.append(Player())

        # get player names
        for player in self.game.players:
            player.name = psg.popup_get_text("Enter your name: ")

        for self.player in range(self.AIplayers):
            if self.__aidifficulty == 'Easy':
                self.game.players.append(EasyAI())
            elif self.__aidifficulty == 'Hard':
                self.game.players.append(HardAI())

        for player in enumerate(self.game.players, start=1):
            if isinstance(player[1], EasyAI) or isinstance(player[1], HardAI):
                player[1].name = "AI " + str(player[0]-self.playernum)
        
        # play game
        while self.game.roundnum < self.game.NUM_ROUNDS:       
            self.roundgui()

        # end sequence

        

        winner = self.game.get_winner()
        
        # get player scores

        playerlist = [player.get_name() for player in self.game.players]
        scorelist = [player.scorecard.get_score() for player in self.game.players]
        # create dictionary of player names and scores
        scorecarddict = sorted(dict(zip(playerlist, scorelist)).items(), key=lambda x: x[1], reverse=True)

        tablelist = []

        # add scores to table
        for key in scorecarddict:
            if scorecarddict[key] == None:
                scorecarddict[key] = 0
            tablelist.append([key, scorecarddict[key]])

            
        scoretable = psg.Table(values = tablelist, headings = ["Player", "Score"], num_rows=(len(self.game.players)), auto_size_columns=True, justification='c')


        layout = [[psg.Text("Game Over!")],
                    [psg.Text(winner.name + " is the winner with a score of " + str(winner.scorecard.get_score()))],
                    [scoretable],
                    [psg.Text("The average score this game was " + str(statistics.mean(scorelist)))],
                    [psg.Button("Back to menu", size = (25, 2))],
                    [psg.Button("Play again", size = (25, 2))],
                    ]

        window = psg.Window("Yahtzee", layout, element_justification='c')

        # add players to leaderboard
        for player in self.game.players:
            # check if player is AI
            if not isinstance(player, EasyAI) and not isinstance(player, HardAI):
                self.addtoleaderboard(player)
        
        while True:
            event, values = window.read()
            if event == "Back to menu":
                window.close()
                self.run()
                break
            elif event == "Play again":
                window.close()
                self.newgame()
                break
            elif event == psg.WIN_CLOSED:
                break
        
        window.close()
        


    # round sequence
    def roundgui(self):
        self.game.roundnum += 1
    
        psg.popup("Round " + str(self.game.roundnum))
        for player in self.game.players:
            if isinstance(player, EasyAI) or isinstance(player, HardAI):
                self.ai_turn_gui(player)
            else:
                self.turngui(player)

    # turn sequence
    def turngui(self, player):

        
        scorecardlist = []
        for key in player.scorecard.keylist:
            scorecardlist.append([key, player.scorecard.scorecard[key]])

      
        playerscoretable = psg.Table(values = scorecardlist, headings = ["Category", "Score"], num_rows=(14), auto_size_columns=True, justification='c')
        
        self.game.rerolls = 0
        self.game.dice.roll()
        #if player.scorecard.score_yahtzee(self.game.dice) == 50:
         #   psg.popup_animated('YahtzeeGIF.gif', background_color=psg.theme_background_color(), time_between_frames=100, no_titlebar = True, auto_close_duration=1000)

        ###########################
        # DYNAMIC OBJECT CREATION #
        ###########################
        
        # create EZboard if option selected

        if self.EZboardopt:
            EZboard = EZBoard(player)
            EZboard.update_scorecard(self.game.dice)
            EZscorecardlist = EZboard.genlist()
            EZboardtable = psg.Table(values = EZscorecardlist, headings = ["Category", " Expected Score"], num_rows=(14), auto_size_columns=True, justification='c')
      
        
            

        
        layout = [
            [psg.Text("Round " + str(self.game.roundnum))],
            [psg.Text(str(player.name) + "'s turn")],
            [playerscoretable] + ([EZboardtable] if self.EZboardopt else []), [psg.Table(values = [[player.scorecard.bonus_calc()]], headings = ['Bonus'], font=20, num_rows=1, justification = 'right')],
            [psg.Text('Your dice are: ' + str(self.game.dice.get_dice()), key='dice')]
        ] + [
            [psg.Button('', image_filename=self.dice_images[dice], image_size=(100, 100), image_subsample=2, button_color=(psg.theme_background_color()), key='dice' + str(index)) for index,dice in enumerate(self.game.dice.get_dice())]
            
        ] + [
            [psg.Text('click dice to reroll, then click reroll button')],
            
            [psg.Button("Reroll")],
            [psg.Text("Enter the number of the category you want to score in")],
            [psg.InputText(tooltip='Enter the number of the category you want to score', key='score_category')],
            [psg.Button("Score")]
        ]
        

        window = psg.Window("Yahtzee", layout, element_justification='c', resizable=True)
        window.finalize()
        window.maximize()
        rerolllist = []

        while True:
            event,values = window.read()
            
            if event == "dice0" and self.game.rerolls < 2:
                rerolllist.append(1)
                #hide dice after click
                window['dice0'].update(visible=False)
            
            if event == "dice1" and self.game.rerolls < 2:
                rerolllist.append(2)
                window['dice1'].update(visible=False)
            
            if event == "dice2" and self.game.rerolls < 2:
                rerolllist.append(3)
                window['dice2'].update(visible=False)

            if event == "dice3" and self.game.rerolls < 2:
                rerolllist.append(4)
                window['dice3'].update(visible=False)
            
            if event == "dice4" and self.game.rerolls < 2:
                rerolllist.append(5) # check this
                window['dice4'].update(visible=False)
            
            

            elif event == "Reroll": 
                if rerolllist == []:
                    psg.popup("No dice selected")
                    continue             
                elif self.game.rerolls < self.game.REROLLS:
                    self.game.rerolls += 1
                    self.game.dice.reroll(rerolllist)
                    for dice in rerolllist:
                        window['dice' + str(dice-1)].update(image_filename=self.dice_images[self.game.dice.get_dice()[dice-1]], image_size=(100, 100), image_subsample=2, button_color=(psg.theme_background_color()), visible=True)
                    rerolllist.clear()
                    
                    # update EZboard if option selected
                    if self.EZboardopt:
                        EZboard.update_scorecard(self.game.dice)
                        EZboardtable.update(EZboard.genlist())

                    
                    if self.game.rerolls == self.game.REROLLS:
                        window['Reroll'].update('No rerolls left')
                    
                    window['dice'].update('Your dice are: ' + str(self.game.dice.get_dice()))
                    #if player.scorecard.score_yahtzee(self.game.dice) == 50:
                    #    psg.popup_animated('YahtzeeGIF.gif', background_color=psg.theme_background_color(), time_between_frames=100, no_titlebar = True)
                    #    break
                          
                else:
                    window['Reroll'].update('No rerolls left')
                    psg.popup("You have used all your rerolls!")
            
            elif event == "Score":
                # check if category choice is valid
                validflag = False
                while True:
                    try:
                        if values['score_category'] == '':
                            psg.popup("No category entered")
                            break
                        elif int(values['score_category']) not in range(1, 14):
                            psg.popup("Invalid choice- must be between 1 and 13")
                            break
                        elif player.scorecard.scorecard[player.scorecard.keylist[int(values['score_category'])-1]] != None:
                            psg.popup("Category already scored")
                            break                            
                        
                        
                        

                        else:
                            validflag = True
                            break
                        
                    except ValueError or TypeError:
                        psg.popup("Invalid choice")
                        break
            
                if validflag:
                    # score category     
                    player.scorecard.score_roll(self.game.dice, int(values['score_category']))
                    window['Score'].update(visible=False)
                    scorecardlist.clear()
                    scorecardlist = player.scorecard.genlist()
                
                    playerscoretable.update(scorecardlist)
                    window.refresh()
                    time.sleep(2) # let user see scorecard
                
                    break
                else:
                    continue
            elif event == psg.WIN_CLOSED:
                del window
                sys.exit()
            
        window.close()

    # play AI turn in GUI
    def ai_turn_gui(self, player):
        player.dice.roll()
        player.play()

        scorecardlist = []
        for key in player.scorecard.keylist:
            scorecardlist.append([key, player.scorecard.scorecard[key]])

      
        playerscoretable = psg.Table(values = scorecardlist, headings = ["Category", "Score"], num_rows=(14), auto_size_columns=True, justification='c')
        
        layout = [
            [psg.Text("Round " + str(self.game.roundnum))],
            [psg.Text(str(player.name) + "'s turn")],
            [playerscoretable],
            [psg.Button("Next turn")]
            
        ]

        window = psg.Window("Yahtzee", layout, size=(700, 600), element_justification='c')
        while True:
            event,values = window.read()
            if event == "Next turn":
                break
            elif event == psg.WIN_CLOSED:
                break
        
        window.close()

    
    # settings page
    def settings(self):
        layout = [
            [psg.Text("Settings")],
            [psg.Text("Theme")],
            [psg.Combo(psg.theme_list(), default_value=self.__theme, key='theme', readonly=True)],
            [psg.T("Dice colour")],
            [psg.Combo(self.dice_colours, default_value='white', key = 'dice_colour', readonly=True)],
            [psg.T("AI difficulty")],
            [psg.Combo(['Easy', 'Hard'], default_value=self.__aidifficulty, key='aidifficulty', readonly=True)], 
            [psg.Checkbox('EZboard', default=self.EZboardopt, key='EZboard')],
            [psg.Button("Apply")]
            
        ]

        window = psg.Window("Settings", layout, element_justification='c')

        while True:
            event, values = window.read()
            if event == "Apply":
                self.__theme = values['theme']
                psg.theme(self.__theme)
                self.__dice_unpack(values['dice_colour'])
                self.__aidifficulty = values['aidifficulty']
                self.EZboardopt = values['EZboard']
                break
            

            elif event == psg.WIN_CLOSED:
                break
        
        window.close()
        

###############################
# USE OF RECURSIVE VALIDATION #
###############################

# gets game mode from user input          
def __get_game_mode():
    game_mode = input("Play in terminal or GUI? (t/g): ")
    if game_mode == "t":
        game = Terminal()
        game.run()
    elif game_mode == "g":
        game = GUI()
        game.run()
    else:
        print("Invalid game mode")
        __get_game_mode()

# main function
if __name__ == "__main__":    
    __get_game_mode()

    







