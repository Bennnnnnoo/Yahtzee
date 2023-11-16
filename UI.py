from Yahtzeegamecode import Game, Player, Scorecard, Dice
import random, math, PySimpleGUI as psg


class GUI:

    def __init__(self):
        self.game = Game()
   

    def run(self):
        psg.popup("Welcome to Yahtzee!")
        self.playernum = int(psg.popup_get_text("Enter the number of players: "))
        for self.player in range(self.playernum):
            self.game.players.append(Player())
        while self.game.roundnum < 13*len(self.game.players):
            self.roundgui()

    def roundgui(self):
        psg.popup("Round " + str(self.roundnum))
        for self.player in self.players:
            self.turngui()


    def turngui(self):
        psg.popup("Player " + str(self.player) + "'s turn")
        self.dice = Dice()
        self.dice.roll()
        self.dicegui = self.dice.get_dice()
        psg.popup("Your dice are: " + str(self.dicegui))
        self.rolls = 0
        while self.rolls < 2:
            self.rolls += 1
            self.keep = psg.popup_get_text("Enter the dice you want to keep: ")
            self.dice.roll(self.keep)
            self.dicegui = self.dice.get_dice()
            psg.popup("Your dice are: " + str(self.dicegui))
        self.category = psg.popup_get_text("Enter the category you want to score in: ")
        self.player.scorecard.score(self.category, self.dice)
        self.roundnum += 1


            
        psg.popup("Game Over!")




game = GUI()
game.run()





