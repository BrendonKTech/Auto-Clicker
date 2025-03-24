import pyautogui
import time
import threading
import tkinter as tk
from tkinter import ttk
import keyboard

clicking = False
click_interval = 5  # Default to 5 seconds
hotkey = "v"  # Default hotkey
mouse_button = "left"  # Default mouse button
click_type = "single"  # Default click type (single or double)


def click_loop():
    """Loop to perform auto-clicking."""
    global clicking
    while clicking:
        if click_type == "single":
            pyautogui.click(button=mouse_button)
        else:
            pyautogui.doubleClick(button=mouse_button)
        time.sleep(click_interval)


def start_clicking():
    """Starts the auto-clicking process."""
    global clicking
    if not clicking:
        clicking = True
        threading.Thread(target=click_loop, daemon=True).start()


def stop_clicking():
    """Stops the auto-clicking process."""
    global clicking
    clicking = False


def toggle_clicking():
    """Toggles clicking state when hotkey is pressed."""
    if clicking:
        stop_clicking()
    else:
        start_clicking()


def update_interval():
    """Updates the click interval based on user input."""
    global click_interval
    try:
        mins = int(min_entry.get()) if min_entry.get().isdigit() else 0
        sec = int(sec_entry.get()) if sec_entry.get().isdigit() else 0
        ms = int(ms_entry.get()) if ms_entry.get().isdigit() else 0

        total_seconds = (mins * 60) + sec + (ms / 1000)
        if total_seconds > 0:
            click_interval = total_seconds
    except ValueError:
        pass


def update_hotkey():
    """Opens a new window to set the hotkey."""
    def set_new_hotkey():
        global hotkey
        new_key = hotkey_entry.get().strip().lower()
        if new_key:
            keyboard.remove_hotkey(hotkey)
            hotkey = new_key
            keyboard.add_hotkey(hotkey, toggle_clicking)
            hotkey_label.config(text=f"Hotkey: {hotkey.upper()}")
            hotkey_window.destroy()

    hotkey_window = tk.Toplevel(root)
    hotkey_window.title("Set Hotkey")
    hotkey_window.geometry("250x100")
    
    tk.Label(hotkey_window, text="Enter new hotkey:").pack(pady=5)
    hotkey_entry = tk.Entry(hotkey_window, width=10)
    hotkey_entry.pack(pady=5)
    
    set_button = ttk.Button(hotkey_window, text="Set Hotkey", command=set_new_hotkey)
    set_button.pack(pady=5)


# Set up hotkey to toggle clicking
keyboard.add_hotkey(hotkey, toggle_clicking)

# Create GUI window
root = tk.Tk()
root.title("Autoclicker")
root.geometry("350x300")
root.resizable(False, False)

# Click Interval Frame
interval_frame = ttk.LabelFrame(root, text="Click Interval")
interval_frame.pack(pady=5, padx=5, fill="both")

tk.Label(interval_frame, text="Minutes:").grid(row=0, column=0, padx=5, pady=5)
min_entry = tk.Entry(interval_frame, width=5)
min_entry.grid(row=0, column=1)
min_entry.insert(0, "0")

tk.Label(interval_frame, text="Seconds:").grid(row=0, column=2, padx=5, pady=5)
sec_entry = tk.Entry(interval_frame, width=5)
sec_entry.grid(row=0, column=3)
sec_entry.insert(0, "5")

tk.Label(interval_frame, text="Milliseconds:").grid(row=0, column=4, padx=5, pady=5)
ms_entry = tk.Entry(interval_frame, width=5)
ms_entry.grid(row=0, column=5)
ms_entry.insert(0, "0")

apply_button = ttk.Button(interval_frame, text="Set Interval", command=update_interval)
apply_button.grid(row=1, column=0, columnspan=6, pady=5)

# Click Options Frame
click_options_frame = ttk.LabelFrame(root, text="Click Options")
click_options_frame.pack(pady=5, padx=5, fill="both")

tk.Label(click_options_frame, text="Mouse Button:").grid(row=0, column=0, padx=5, pady=5)
mouse_button_var = tk.StringVar(value="left")
mouse_button_menu = ttk.Combobox(click_options_frame, textvariable=mouse_button_var, values=["left", "right", "middle"], state="readonly")
mouse_button_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(click_options_frame, text="Click Type:").grid(row=1, column=0, padx=5, pady=5)
click_type_var = tk.StringVar(value="single")
click_type_menu = ttk.Combobox(click_options_frame, textvariable=click_type_var, values=["single", "double"], state="readonly")
click_type_menu.grid(row=1, column=1, padx=5, pady=5)


def update_click_options():
    global mouse_button, click_type
    mouse_button = mouse_button_var.get()
    click_type = click_type_var.get()


apply_click_button = ttk.Button(click_options_frame, text="Apply Click Options", command=update_click_options)
apply_click_button.grid(row=2, column=0, columnspan=2, pady=5)

# Hotkey Settings Frame
hotkey_frame = ttk.LabelFrame(root, text="Hotkey Settings")
hotkey_frame.pack(pady=5, padx=5, fill="both")

hotkey_label = tk.Label(hotkey_frame, text=f"Hotkey: {hotkey.upper()}", fg="red")
hotkey_label.pack(pady=5)

hotkey_button = ttk.Button(hotkey_frame, text="Change Hotkey", command=update_hotkey)
hotkey_button.pack(pady=5)

# Run the GUI
root.mainloop()
