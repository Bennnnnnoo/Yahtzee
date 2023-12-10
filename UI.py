from Yahtzeegamecode import Game, Player, Scorecard, Dice
import random, math, PySimpleGUI as psg, time



class Terminal:
    


        
        def __init__(self):

            self.game = Game()

            
            
        def run(self):
            

            while True:
                try:
                    self.game.playernum = int(input("Enter the number of players: "))
                    break
                except ValueError:
                    print("Invalid number of players")
                    continue
                    

                
            
            for player in range(self.game.playernum):
                self.game.players.append(Player())

            for player in self.game.players:
                player.name = input("Enter your name: ")
    
            while self.game.roundnum < 13:
                self.tround()

            print('Game Over!')
            
            for player in self.game.players:
                print(player.name + "'s score is: " + str(player.scorecard.get_total_score()))
                print('the winner is'+ self.game.get_winner() + 'with a score of' + self.game.get_winner.score())

            

            
            
        def get_reroll_choice(self):
            reroll_list = input("Enter the dice indexes you want to reroll: ").split(',')
            reroll_list = [int(i) for i in reroll_list]
            return reroll_list
            

        def get_category_choice(self,player):
            try:
                choice = (int(input("Enter your choice: ")))
            
            except ValueError or TypeError:
                print("Invalid choice")
                choice = self.get_category_choice(player)

            if choice not in range(1, 14):
                print("Invalid choice- must be between 1 and 13")
                choice = self.get_category_choice(player)
            #prevent user from choosing same option twice

            
            if player.get_scorecard().scorecard[player.scorecard.keylist[choice-1]] != None:
                print("Category already scored")
                choice = self.get_category_choice(player)
            # check later

            return choice  
            
        def tround(self):

            self.game.roundnum += 1

            print("Round " + str(self.game.roundnum))
            for player in self.game.players:
                self.turn(player)
                
        def turn(self,player):

            
            print(player.name + "'s turn")
            self.game.dice.roll()
            print("Your dice are: " + str(self.game.dice.get_dice()))
            while self.game.rerolls < self.game.REROLLS:
                self.game.rerolls += 1
                self.game.dice.reroll(self.get_reroll_choice())
                print("Your dice are: " + str(self.game.dice.get_dice()))
            self.game.rerolls = 0
            player.scorecard.show_scorecard()
            choice = self.get_category_choice(player)
            player.scorecard.score_roll(self.game.dice, choice)
            player.scorecard.show_scorecard()


                

                


            


    
    
        '''def turngui(self):
            print("Player " + str(self.player) + "'s turn")
            self.dice = Dice()
            self.dice.roll()
            self.dicegui = self.dice.get_dice()
            print("Your dice are: " + str(self.dicegui))
            self.rolls = 0
            while self.rolls < 2:
                self.rolls += 1
                self.keep = input("Enter the dice you want to keep: ")
                self.dice.roll(self.keep)
                self.dicegui = self.dice.get_dice()
                print("Your dice are: " + str(self.dicegui))
            self.category = input("Enter the category you want to score in: ")
            self.player.scorecard.score(self.category, self.dice)
            self.game.roundnum += 1
    
    
                
            print("Game Over!")'''

class GUI:

    def __init__(self):
        self.game = Game()
   



    def run(self):
        psg.theme("DarkGreen1")

        


        layout = [[psg.Text("Welcome to Yahtzee!")],
                  [psg.T("")],
                  [psg.Button("Start new Game", size = (50, 5) )],
                  [psg.T("")],
                  [psg.Button("Load Game",size = (50, 5) )],
                  [psg.T("")],
                  [psg.Button("Leaderboard", size = (50, 5))], 
                  [psg.T("")],
                  [psg.Button("Rules", size = (50, 5))],
                  ]
                  
        window = psg.Window("Yahtzee", layout, size=(700, 700), element_justification='c')
        while True:
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
            elif event == psg.WIN_CLOSED:
                break
        window.close()




    def newgame(self):
        self.game = Game()


        self.playernum = int(psg.popup_get_text("Enter the number of players: "))
        for self.player in range(self.playernum):
            self.game.players.append(Player())
        for player in self.game.players:
            player.name = psg.popup_get_text("Enter your name: ")

        while self.game.roundnum < 13*len(self.game.players):
            self.roundgui()

        psg.popup("Game Over!")

        

        self.run()
        



    def roundgui(self):
        self.game.roundnum += 1
        psg.popup("Round " + str(self.game.roundnum))
        for player in self.game.players:
            self.turngui(player)


    def turngui(self, player):

        # makes scorecard dict to 2d array for easy table reading

        scorecardlist = []
        for key in player.scorecard.keylist:
            scorecardlist.append([key, player.scorecard.scorecard[key]])

        # table initialisation
        playerscoretable = psg.Table(values = scorecardlist, headings = ["Category", "Score"], num_rows=(14), auto_size_columns=True, justification='c')
        
        # variable initialisaion
        self.game.rerolls = 0
        self.game.dice.roll()
        
        # layout
        layout = [
            [psg.Text("Round " + str(self.game.roundnum))],
            [psg.Text(str(player.name) + "'s turn")],
            [playerscoretable],
            [psg.Text('Your dice are: ' + str(self.game.dice.get_dice()), key = 'dice')],
            [psg.Text('Enter the dice you want to reroll: ')],[psg.Input(key='reroll')],
            [psg.Button("Reroll")],
            [psg.Input(key='score_category')],
            [psg.Button("Score")],




       ]
        





        window = psg.Window("Yahtzee", layout, size=(700, 500), element_justification='c')
        while True:
            event,values = window.read()
            if event == "Reroll":
                
                if self.game.rerolls < self.game.REROLLS:
                    self.game.rerolls += 1
                    self.game.dice.reroll(values['reroll'].split(','))
                    window['reroll'].update('')
                    window['dice'].update('Your dice are: ' + str(self.game.dice.get_dice()))
                else:
                    psg.popup("You have used all your rerolls!")
            elif event == "Score":
                player.scorecard.score_roll(self.game.dice, int(values['score_category']))
                window['Score'].update(visible=False)
                scorecardlist.clear()
                for key in player.scorecard.keylist:
                    scorecardlist.append([key, player.scorecard.scorecard[key]])
                
                playerscoretable.update(scorecardlist)
                time.sleep(1)
                
                break
            elif event == psg.WIN_CLOSED:
                break
            
        window.close()



    ''' rolls = 0
        psg.popup(str(player.name) + "'s turn")
        self.game.dice = Dice()
        self.game.dice.roll()
        
        psg.popup("Your dice are: " + str(self.game.dice.get_dice()))
        self.rolls = 0
        while rolls < 2:
            rolls += 1
            rerolls = psg.popup_get_text("Enter the dice you want to keep: ")
            self.dice.roll(rerolls)
            psg.popup("Your dice are: " + str(self.game.dice.get_dice()))
        self.category = psg.popup_get_text("Enter the category you want to score in: ")
        player.scorecard.score_roll(self.game.dice, int(self.catgory))
        self.roundnum += 1 '''


            
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


if __name__ == "__main__":    # Main function
    __get_game_mode()

    







