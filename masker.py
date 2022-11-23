from PIL import Image, ImageGrab, ImageEnhance
from PIL.ImageQt import ImageQt
import pyautogui as pag
import numpy

class PyMasker():
    def __init__(self):
        super().__init__()

        self.movement_threshold = 7
        self.full_capture_area = 150
        self.capture_area = self.full_capture_area/2

        self.capture_around_cursor = True
        self.capture_around_fixed = False

    def strip_color(self, image):
        stripped_img = image.convert('L')
        
        contrast_enhancer = ImageEnhance.Contrast(stripped_img)
        stripped_img = contrast_enhancer.enhance(1.5)

        brightness_enhancer = ImageEnhance.Brightness(stripped_img)
        stripped_img = brightness_enhancer.enhance(1.5)

        return stripped_img

    def find_movement(self):
         a = "b" #placeholder

    def raw_img_from_cursor(self):
        x, y = pag.position()
        inc = self.capture_area
        image = ImageGrab.grab(bbox=(x-inc, y-inc, x+inc, y+inc))
        return image

    def offset_img_from_cursor(self):
        x, y = pag.position()
        image = ImageGrab.grab(bbox=(x, y, x+150, y+150))
        return image