from pynput.mouse import Listener as mouse
from pynput import keyboard
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(message)s')

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('{0},{1},{2},null'.format(x, y, button))

def on_press(key):
    print(key)
    logging.info('null,null,null,{0} '.format(key))

with mouse(on_click=on_click, 
) as listenerM, keyboard.Listener(on_press=on_press) as listenerKB:
    listenerM.join()
    listenerKB.join()

