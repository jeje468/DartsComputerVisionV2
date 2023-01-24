from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from calibrate import *
from kivy.properties import StringProperty

#define our different screens
class MainWindow(Screen):
    def setup(self):
        self.manager.get_screen("gameplay").ids.player_label.text = self.manager.get_screen("add_player").ids.players_label.text.split(", ")[0]
        GameplayWindow.players = self.manager.get_screen("add_player").ids.players_label.text.split(", ")
        GameplayWindow.calibrationPoints = calibrate()
        
class GameplayWindow(Screen):
    players = []
    currentPlayerIdx = 0
    currentPlayerName = StringProperty("")
    calibrationPoints = []

    def nextPlayer(self):
        self.ids.gameplay_points_label.text = "0"
        self.currentPlayerName = self.players[self.currentPlayerIdx % len(self.players)]
        self.currentPlayerIdx += 1

    def onePlayersRound(self):
        playerPointsLabel = ""
        playersPoints = startGame(self.calibrationPoints)

        for i in range (0, len(playersPoints)):
            if i == 0:
                playerPointsLabel += str(playersPoints[i])
            else:
                playerPointsLabel += " + " + str(playersPoints[i])
        
        self.ids.gameplay_points_label.text = playerPointsLabel
        print("Next player")

        #self.ids.gameplay_points_label.text = "0"

        if self.currentPlayerIdx == 1:
            self.ids.gameplay_button.text = "Next player"

    def on_currentPlayerName(self, instance, value):
        self.text = value

class AddPlayerWindow(Screen):
    def addPlayer(self):
        if self.ids.players_label.text == "":
            self.ids.players_label.text = self.ids.player_text_input.text
        else:
            self.ids.players_label.text += ", " + self.ids.player_text_input.text

        self.ids.player_text_input.text = ""
    
    def removePlayer(self):
        playersLabel = self.ids.players_label.text
        players = playersLabel.split(", ")
        players.pop()

        playersLabel = ""
        
        for i in range (0, len(players)):
            if i == 0:
                playersLabel = players[i]
            else:
                playersLabel += ", " + players[i]
        
        self.ids.players_label.text = playersLabel


class CalibrationWindow(Screen):
    calibrationLabelValues = ["Top camera empty", "Top camera left", "Top camera right", "Bottom camera empty", "Bottom camera top", "Bottom camera bottom"]
    idx = 0

    def takeCalibrationPhoto(self):
        takePhoto()

        self.idx += 1
        
        if self.idx < len(self.calibrationLabelValues):
            self.ids.calibration_label.text = self.calibrationLabelValues[self.idx]
        
        if idx == 5:
            self.ids.calibration_button.disabled = True

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('AppMain.kv')

class MyLayout(Widget):
    pass

class DartsApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    DartsApp().run()