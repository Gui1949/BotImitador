import pyautogui
import time
import os
import argparse
import sys
from tkinter import *
from tkinter import ttk

# --- Configuration and Arguments ---
parser = argparse.ArgumentParser("bot")
parser.add_argument("-c", "--chosen_file", help="Preset file number", type=str)
parser.add_argument("-l", "--loop", help="Loop or not", type=str)
parser.add_argument("-t", "--loop_timeout", help="Loop timeout in seconds", type=int)
parser.add_argument("-d", "--delay", help="Delay between every command", type=int)
args = parser.parse_args()


preset_files = [f for f in os.listdir("presets") if f.endswith(".txt")]
if not preset_files:
    print("No preset files found in 'presets' directory. Exiting.")
    exit()

chosen_file = args.chosen_file
loop_choice = args.loop
loop_timeout = args.loop_timeout
delay = args.delay

# Terminal input if arguments not provided
if not chosen_file:
    for i, file in enumerate(preset_files):
        print(f"{i}. {file}")
    chosen_file = input("Preset Number: ")
    loop_choice = input("Loop? (y/n): ")
    loop_timeout = int(input("Timeout (seconds): ") if loop_choice == 'y' else 0)

# Loading preset file
file_index = int(chosen_file)
selected_filename = preset_files[file_index]
file_path = os.path.join("presets", selected_filename)

mouse_movements = []
with open(file_path, "r") as f:
    for line in f.readlines():
        coords = line.strip().split(",")
        if len(coords) < 2: continue
        x = int(coords[0]) if coords[0] != 'null' else 'null'
        y = int(coords[1]) if coords[1] != 'null' else 'null'
        c = 1 if coords[2] != 'null' else 0
        k = coords[3] if coords[3] != 'null' else 'null'
        ts = float(coords[4]) if len(coords) > 4 else 0
        mouse_movements.append([x, y, c, k, ts])

# --- Execution Logic ---
def run_bot():

    last_time = 0
    for x, y, c, k, timestamp in mouse_movements:
        time_to_wait = timestamp - last_time + (delay if delay else 0)
        if time_to_wait > 0:
            time.sleep(time_to_wait)
        
        if x != 'null':
            pyautogui.moveTo(x, y)
        if c == 1:
            pyautogui.click()
        if k != 'null':
            key = k.replace("'", "")
            if 'Key.' in key:
                pyautogui.press(key.replace('Key.', ''))
            else:
                pyautogui.typewrite(key)
        last_time = timestamp
    
    if loop_choice == 'y':
        start_countdown(loop_timeout)
    else:
        status_var.set("Status: Finished.")
        root.after(1000, root.destroy)

def start_countdown(seconds):
    if seconds > 0:
        status_var.set(f"Status: Waiting for next loop...")
        timer_var.set(f"Next execution in: {seconds}s")
        # Schedule the update for the next second
        root.after(1000, lambda: start_countdown(seconds - 1))

        if seconds == 60 or seconds == 30 or seconds == 10 or seconds <= 5:
            root.focus_force()
            root.bell()

    else:
        timer_var.set("Next execution in: 0s")
        run_bot()

# --- Window Setup ---

root = Tk()
root.title("Bot Executor")
root.geometry("400x250")

status_var = StringVar(value="Status: Starting...")
timer_var = StringVar(value="Next execution in: --")

frm = ttk.Frame(root, padding=20)
frm.pack(expand=True, fill="both")

# Preset Info
ttk.Label(frm, text=f"File: {selected_filename}", font=("Helvetica", 10, "bold")).pack(pady=5)
ttk.Label(frm, text=f"Loop: {'Yes' if loop_choice == 'y' else 'No'}").pack()
ttk.Label(frm, text=f"Timeout: {loop_timeout}s").pack()

ttk.Separator(frm, orient=HORIZONTAL).pack(fill=X, pady=10)

# Dynamic Status and Timer
ttk.Label(frm, textvariable=status_var, foreground="blue").pack()
ttk.Label(frm, textvariable=timer_var, font=("Helvetica", 12, "bold")).pack(pady=10)

# Exit Button
ttk.Button(frm, text="Exit / Stop", command=root.destroy).pack(side=BOTTOM)

# Start the bot after the mainloop starts
root.after(1000, run_bot)

root.mainloop()