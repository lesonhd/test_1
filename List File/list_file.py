import os
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog

# root_tk = Tk()

my_path = filedialog.askdirectory(title = 'Chọn một Folder')
my_list = []
for root , dirs , files in os.walk(my_path):
    for f in files:
        my_list.append(f)

dwg = {"DWG": pd.Series(my_list)}

df = pd.DataFrame(dwg)
df.to_excel('List dwg.xlsx')