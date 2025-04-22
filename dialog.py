import csv
import ctypes
import shutil
import tkinter as tk
from datetime import datetime
from tkinter import filedialog


WIDTH = shutil.get_terminal_size().columns

def select_file(t):
    # Create the root window & inital window.
    root = tk.Tk()
    root.withdraw()

    # Open file about Host Arrary & Check file have or value.
    try:
        file = filedialog.askopenfilename(
            defaultextension=f'.{t}',
            title="Open File",
            filetypes=[("Text files", f"*.{t}"), ("All files", "*.*")]
        )
    except KeyboardInterrupt:
        # Delete root window.
        root.destroy()

    # Convert value in file to array list.
    if "txt" != t:
        with open(file, newline='') as f:
            return list(csv.DictReader(f))
    else:
        return open(file, 'r').readlines()

def save_file(r):
    # Date time now.
    now = datetime.now()
    strtime = now.strftime("%Y-%m-%dT%H%M%S")

    root = tk.Tk()
    root.withdraw()
    fn = filedialog.asksaveasfilename(
        initialfile=f"search-url-{strtime}",
        defaultextension='.csv',
        title="Save File As",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if fn:
        try:
            with open(fn, 'w', newline='') as f:
                writer = csv.writer(f)
                # Header
                field = ['URI', 'Response', "Source"]
                # Write header in file.
                writer.writerow(field)
                # Write row data.
                writer.writerows(r)

            # ctypes.windll.user32.MessageBoxW(0, "File saved successfully:\n{}".format(fn), "File Saved", 0)
        except Exception as e:
            pass
            # ctypes.windll.user32.MessageBoxW(0, "Error saving file:\n{}".format(str(e)), "Error", 0)

    root.destroy()
    print("Save file success...".center(WIDTH))
    print('=' * WIDTH)
