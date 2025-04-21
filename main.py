import os
from itertools import groupby
import tkinter as tk
import csv
import ctypes
from datetime import datetime
from tkinter import filedialog


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

def process(a, b):
    res = []
    for i in a:
        for j in b:
            if i in j:
                res.append(f"'{i}' must to Bypass in WSA ‼️")
    return [i for i,_ in groupby(res)]

if __name__ == "__main__":
    while True:
        try:
            print("Select the input file list about URL: ")
            a = [i.rstrip() for i in select_file("txt")]
            print("Select the input file CSV from WSA: ")
            b = [i['Domain or IP'] for i in select_file("csv")]
            r = process(a,b)
            print("Result have found in the WSA!!: ")
            print('#################################')
            if len(r) != 0:
                for i in r:
                    print(i)
                    print('=================================')
            else:
                print("Empty not have to Bypass in WSA ❤️")
            input('press "Enter" to contiunes....')
        except Exception:
            sys.exit(0)
