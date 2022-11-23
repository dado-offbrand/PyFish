from screeninfo import get_monitors
import pyautogui as pag

class PyFisher():
    def __init__(self):
        super().__init__()

        self.should_cast = False
        self.casted = False
        self.x = 0
        self.y = 0

    def update_positions(self):
        self.x = get_monitors([0]).width/2
        self.y = get_monitors([0]).height/2

    def cast_hook(self):
        self.update_positions()
        pag.leftClick(self.x, self.y)
        self.casted = True

    def reel_hook(self):
        self.update_positions()
        pag.leftClick(self.x, self.y)
        self.casted = False