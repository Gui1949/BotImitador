from pynput.mouse import Listener as mouse
from pynput import keyboard
import logging
import time

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(message)s')

start_time = time.time()

def on_click(x, y, button, pressed):
    if pressed:
        current_time = time.time() - start_time
        logging.info('{0},{1},{2},null,{3}'.format(x, y, button, current_time))

def on_press(key):
    print(key)
    current_time = time.time() - start_time
    logging.info('null,null,null,{0},{1}'.format(key, current_time))
    
    if key == keyboard.Key.esc:
        return False

with mouse(on_click=on_click) as listenerM:
    with keyboard.Listener(on_press=on_press) as listenerKB:
        listenerKB.join()
        listenerM.stop()

