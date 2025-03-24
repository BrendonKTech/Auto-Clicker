# Autoclicker GUI

## Overview
This is a simple and efficient autoclicker with a graphical user interface built using Python and Tkinter. It allows users to automate mouse clicks with customizable settings such as interval timing, mouse button selection, and click type (single or double).

## Features
- Set custom click intervals (minutes, seconds, milliseconds)
- Choose between single or double clicks
- Select mouse button (left, right, or middle)
- Assign a custom hotkey to start/stop clicking
- Simple and intuitive UI

## How to Use
### 1. Running the Autoclicker
1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Install dependencies by running:
   ```sh
   pip install pyautogui keyboard
   ```
4. Run the script:
   ```sh
   python autoclicker.py
   ```

### 2. Setting Click Intervals
- Enter the desired click interval in minutes, seconds, and milliseconds.
- Click the "Set Interval" button to apply changes.

### 3. Configuring Click Options
- Choose the mouse button (left, right, middle) from the dropdown menu.
- Select single or double click mode.
- Click "Apply Click Options" to save changes.

### 4. Setting a Custom Hotkey
- Click "Change Hotkey" to open the hotkey configuration window.
- Enter the new hotkey and save it.
- The hotkey will be displayed in the main window.

## Requirements
- Python 3.x
- `pyautogui`
- `keyboard`
- `tkinter` (included in Python by default, unless using macOS, Linux)

## Notes
- Ensure you run the script with Python installed and dependencies installed.

## License
This project is open-source and available for modification and distribution.

