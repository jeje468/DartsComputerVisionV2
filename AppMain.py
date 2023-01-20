from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from calibrate import *

#define our different screens
class MainWindow(Screen):
    pass


class CalibrationWindow(Screen):
    def takeCalibrationPhoto(self):
        idx, label = takePhoto()
        self.ids.calibration_label.text = label

        if idx == 6:
            self.ids.calibration_button.disabled = True

class GameplayWindow(Screen):
    def startGame(self):
        playerPointsLabel = ""
        calibrationPoints = calibrate()
        playersPoints = startGame(calibrationPoints)

        for i in range (0, len(playersPoints)):
            if i == 0:
                playerPointsLabel += str(playersPoints[i])
            else:
                playerPointsLabel += " + " + str(playersPoints[i])
        
        self.ids.gameplay_points_label.text = playerPointsLabel

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