import sys
import multiprocessing
from dialog import select_file, save_file
from process import process


if __name__ == "__main__":
    multiprocessing.set_start_method('fork')

    while True:
        try:
            print("Select the input file list about URL: ")
            a = [i.rstrip() for i in select_file("txt")]
            print("Select the input file CSV from WSA: ")
            b = [[i['Domain or IP'], i['Transactions Completed'], i['Transactions Blocked']] for i in select_file("csv")]
            r = process(a,b)
            if len(r) != 0:
                print("\nBrowse to save file result: ")
                print('=========================================')
                _ = save_file(r)
            else:
                print("Result: ")
                print('=========================================')
                print("Empty not found in the Proxy.")
                print('=========================================')
            input('press "Enter" to contiunes....')
        except Exception:
            sys.exit(0)
