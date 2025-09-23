import pyautogui
import time
import os

# Parse the log file
mouse_movements = []


# Prompt the user to choose a file from the presets folder
preset_files = [f for f in os.listdir("presets") if f.endswith(".txt")]
if not preset_files:
    print("No .txt files found in the presets folder.")
    exit()

# Print a list of the preset files
print("Select a preset file from the following list:")
for i, file in enumerate(preset_files):
    print(f"{i}. {file}")

# Prompt the user to choose a file
chosen_file = input("Enter the number of the preset file you want to use: ")
loop = input("Loop? y/n")

# Validate the user's input
try:
    chosen_file = int(chosen_file)
except ValueError:
    print("Invalid input.")
    exit()

# Check if the user's choice is valid
if chosen_file < 0 or chosen_file >= len(preset_files):
    print("Invalid file choice.")
    exit()

# Construct file path
file_path = os.path.join("presets", preset_files[chosen_file])

with open(file_path, "r") as f:
    for line in f.readlines():
        coords = line.strip().split(",")
        x = coords[0]
        y = coords[1]
        c = 0
        k = 0
        timestamp = float(coords[4]) if len(coords) > 4 else 0

        if(x != 'null'):
            x = int(x)
            y = int(y)

        if(coords[2] != 'null'):
            print(coords[2])
            c = 1

        if(k != 'null'):
            k = coords[3]   

        coords = [x,y,c,k,timestamp] 
        mouse_movements.append(coords)

# Infinite Loop
if(loop == 'y'):
    while True:
        last_time = 0
        # Replay the mouse movements
        for x, y, c, k, timestamp in mouse_movements:
            # Wait for the correct timing
            time_to_wait = timestamp - last_time
            if time_to_wait > 0:
                time.sleep(time_to_wait)
            
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
            
            last_time = timestamp
        time.sleep(2)
