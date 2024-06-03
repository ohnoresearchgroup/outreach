# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:28:06 2024

@author: peo0005
"""

import serial
import tkinter as tk
from tkinter import ttk

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Function to read from the serial port and update the label
def read_from_serial():
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if is_number(line):
                number_label.config(text=line)
    except Exception as e:
        print(f"Error reading from serial port: {e}")
    
    # Schedule the function to be called again after 100 ms
    root.after(100, read_from_serial)

# Set up the serial port
try:
    ser = serial.Serial('COM3', 115200, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# Set up the GUI
root = tk.Tk()
root.title("VOC Reader")

# Add header label
header_label = ttk.Label(root, text="VOC concentration [ppb]", font=('Helvetica', 24))
header_label.pack(padx=20, pady=10)

number_label = ttk.Label(root, text="Waiting for data...", font=('Helvetica', 48))
number_label.pack(padx=20, pady=20)

# Start reading from the serial port
read_from_serial()

# Start the Tkinter main loop
root.mainloop()

# Close the serial port when the application is closed
ser.close()
