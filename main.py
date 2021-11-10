# Python File Organzier
# Created by Fabrice Souffrant on 11/9/21
# Upgraded on N/A

import time
import datetime
import os

import tkinter as tk
from tkinter import filedialog


# Functions
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print("Select file containing settings and name of guards: ")
x = open(file_path)
