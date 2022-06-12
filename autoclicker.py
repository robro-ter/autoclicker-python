from enum import auto
from pynput.mouse import Button, Controller
from pynput import mouse
import keyboard as no
import time
import multiprocessing as mp
thingy = Controller()
def multi():
    while 1:
        if no.is_pressed('`'):
            time.sleep(.0001)
            thingy.click(Button.left,3)
        if no.is_pressed('\\'):
            time.sleep(.0001)
            thingy.click(Button.right,3)
if __name__ == "__main__":
    p1 = mp.Process(target=multi)
    p1.start()