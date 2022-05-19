from PIL import ImageGrab, Image
import pyautogui
import keyboard

while True:
    image = ImageGrab.grab()
    color = image.getpixel((pyautogui.position()))
    if color == (75, 219, 106) or color == (43, 135, 209):
        pyautogui.click(pyautogui.position())   
    if keyboard.is_pressed('space'):
        exit()
