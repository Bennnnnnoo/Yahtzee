from Yahtzeegamecode import Game, Player, Scorecard, Dice
import random, math, PySimpleGUI as psg


class GUI:

    def __init__(self):
        self.game = Game()
        self.players = []
        self.player = Player()
        self.scorecard = Scorecard()
        self.dice = Dice()
        self.roundnum = 0
        self.rerolls = 0
        self.roll = []
        self.score = 0
        self.bonus = 0
        self.upper_score = 0
        self.lower_score = 0
        self.total_score = 0
        self.name = ""
        self.players = 0

    def run(self):
        psg.popup("Welcome to Yahtzee!")
        self.players = int(psg.popup_get_text("Enter the number of players: "))
        for self.player in range(self.players):
            self.players.append(Player())
        while self.roundnum < 13*len(self.players):
            self.round()

            
        psg.popup("Game Over!")




game = GUI()
game.run()



