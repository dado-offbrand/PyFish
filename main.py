# PyQt5 reserved
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont

# Misc reserved
from PIL.ImageQt import ImageQt
import pyautogui as pag
import sys

# Script reserved
import fisher
import masker
import events

#----------------------------------------------------------------#
# MAIN PYFISH CLASS
#----------------------------------------------------------------#

class PyfishMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.fisher = fisher.PyFisher()
        self.masker = masker.PyMasker()
        self.events = events.Eventhandler()

        self.events.set_window(self)
        self.window_title = 'PyFish'
        self.create_ui()

    def create_ui(self):
        self.rod_previews = QLabel("Rod Previews")

        self.img_left = QLabel()
        self.img_right = QLabel()

        self.thresh_label = QLabel("Movement Threshold (px)")
        self.thresh_input = QLineEdit()

        self.picture_centered_cb = QCheckBox("Picture centered at cursor")
        self.picture_offset_cb = QCheckBox("Picture is offset from cursor")

        self.window_layout = QGridLayout()
        self.main_font = QFont('Arial', 10)

        self.config_ui()

    def config_ui(self):
        self.setWindowTitle(self.window_title)
        self.window_layout.setHorizontalSpacing(5)

        self.window_layout.addWidget(self.rod_previews, 0, 0)
        self.window_layout.addWidget(self.img_left, 1, 0)
        self.window_layout.addWidget(self.img_right, 1, 1)
        self.window_layout.addWidget(self.thresh_label, 2, 0)
        self.window_layout.addWidget(self.thresh_input, 3, 0)
        self.window_layout.addWidget(self.picture_centered_cb, 4, 0)
        self.window_layout.addWidget(self.picture_offset_cb, 5, 0)

        self.rod_previews.setFont(self.main_font)
        self.thresh_label.setFont(self.main_font)
        self.picture_centered_cb.setFont(self.main_font)
        self.picture_offset_cb.setFont(self.main_font)

        self.picture_centered_cb.setChecked(True)

        self.setLayout(self.window_layout)
        self.add_actions()
        self.show()

    def add_actions(self):
        self.picture_centered_cb.toggled.connect(self.events.toggle_check_centered)
        self.picture_offset_cb.toggled.connect(self.events.toggle_check_offset)
        self.thresh_input.textEdited.connect(self.events.filter_threshold)

    def update_previews(self):
        untouched_prev = self.masker.raw_img_from_cursor()
        stripped_prev = self.masker.strip_color(untouched_prev)
        
        # can't convert in masker class because of how color stripping works
        untouched_prev = ImageQt(untouched_prev)
        stripped_prev = ImageQt(stripped_prev)

        self.img_left.setPixmap(QPixmap(QPixmap.fromImage(untouched_prev)))
        self.img_right.setPixmap(QPixmap(QPixmap.fromImage(stripped_prev)))
    
#----------------------------------------------------------------#
# INITIATE GUI (CLIENT)
#----------------------------------------------------------------#

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = PyfishMainWindow()
    window.update_previews()
    window.show()

    sys.exit(app.exec_())