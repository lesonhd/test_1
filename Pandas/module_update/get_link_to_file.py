from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
# from openpyxl import load_workbook
# Root_tk = Tk()
mFolder = filedialog.askdirectory(title='Chọn Folder update Fit-up')
def Get_fit_up_file (input_folder:)
    m_Files = []
    for links, folders, files in os.walk(input_folder):
        for file in files:
                f = [os.path.join(links,file)] # không hiểu vì sao sử dụng dấu ngoặc vuông lại được
                m_Files.extend(f)
return m_Files

# wb = load_workbook(m_Files[0])
# ws = wb.worksheets[0]

# print(ws['I7'].value)