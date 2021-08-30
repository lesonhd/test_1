import os
import pandas as pd
import numpy as np
import shutil
from tkinter import *
from tkinter import filedialog

root_tk = Tk()
my_path_dwg = filedialog.askdirectory(title ='Chon Folder Bản vẽ Nguồn')
my_path_copy = filedialog.askdirectory(title ='Chọn Folder bản vẽ copy')

#  Tạo 1 list trống là list của các đường link của các file trong folder
my_files = []

for root , dirs , files in os.walk(my_path_dwg):
    #  in ra đường link của các folder
    # print(root) 
    #  In ra các list là tên của folder cấp 1, folder cấp 2
    # print(dirs)
    #  in ra các list tên của các file trong từng folder
    # print(files)

    # Tạo list bao gồm đường link của tất cả các file trong folder
    my_files.extend([os.path.join(root,f) for f in files])

#  Lấy tên file của các đường link đến file ở list đã tạo bên trên
# for f in my_files:
#     print(os.path.basename(f))

df = pd.read_excel('file_copy.xlsx')
dic_ten_file = pd.DataFrame.to_dict(df)
list_ten_file = list(dic_ten_file['Dwg'].values())

for f1 in list_ten_file:
    for f2 in my_files:
        if f1 == os.path.basename(f2):
            shutil.copy(f2,my_path_copy)








