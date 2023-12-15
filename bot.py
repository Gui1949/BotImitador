import pyautogui
import time

# Parse the log file
mouse_movements = []
with open("mouse_log.txt", "r") as f:
    for line in f.readlines():
        coords = line.strip().split(",")
        x = coords[0]
        y = coords[1]
        c = 0
        k = 0

        if(x != 'null'):
            x = int(x)
            y = int(y)

        if(coords[2] != 'null'):
            print(coords[2])
            c = 1

        if(k != 'null'):
            k = coords[3]   

        coords = [x,y,c,k] 

        mouse_movements.append(coords)



    
# Replay the mouse movements
for x, y, c, k in mouse_movements:

    if(x != 'null'):
        print(x,y)
        pyautogui.moveTo(x, y)

    if(c == 1):
        pyautogui.click()

    if(k != 'null'):
        key = k.replace("'","")

        if(key.find('.')):
            pyautogui.press(key.replace('Key.', ''))
        else:
            pyautogui.typewrite(key)



# Optionally, add a delay between movements to match the timestamps
# for i, (x, y) in enumerate(mouse_movements):
#     if i > 0:
#         time.sleep(mouse_movements[i-1][2] - mouse_movements[i][2])
#     pyautogui.moveto(x, y)
