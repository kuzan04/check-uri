import os
import sys
import shutil
import multiprocessing
from dialog import select_file, save_file
from process import process


WIDTH = shutil.get_terminal_size().columns

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    if sys.platform != "win32" and sys.platform != "cygwin" and sys.platform != "msys":
         multiprocessing.set_start_method('fork')

    while True:
        try:
            clear_screen()
            print("Select the input file list about URL: ")
            a = [i.rstrip() for i in select_file("txt")]
            print("Select the input file CSV from WSA: ")
            print('=' * WIDTH)
            b = [[i['Domain or IP'], i['Transactions Completed'], i['Transactions Blocked']] for i in select_file("csv")]
            r = process(a,b)
            print('=' * WIDTH)
            if len(r) != 0:
                print("Browse to save file result: ".center(WIDTH))
                print('=' * WIDTH)
                _ = save_file(r)
            else:
                print("Result: ")
                print('=' * WIDTH)
                print("Empty not found in the Proxy.")
                print('=' * WIDTH)
            try:
                input('press "Enter" to contiunes....')
            except KeyboardInterrupt:
                sys.exit(0)
        except Exception:
            sys.exit(0)
