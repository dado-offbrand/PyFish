from PyQt5.QtWidgets import QApplication

class Eventhandler():
    def __init__(self):
        super().__init__()
        self.window = None

    def set_window(self, window):
        self.window = window

    def toggle_check_centered(self, checked):
        self.window.picture_offset_cb.setChecked(False)

    def toggle_check_offset(self, checked):
        self.window.picture_centered_cb.setChecked(False)

    def filter_threshold(self):
        #text = threshold_qedit.text
        # strip text of non-numeric characters
        self.window.thresh_input.text = "totally filtered"