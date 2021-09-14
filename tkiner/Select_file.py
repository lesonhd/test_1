from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os

Root_tk = Tk()

# mở file luôn
# m_file = filedialog.askopenfile(title="Chon File cần mở")
# Lấy tên file theo dòng lệnh trên
# m_file.name

# Lấy trực tiếp tên file để mở

file_2 = filedialog.askopenfilename(title="chọn file")


#  mở file bằng os khi file ko cần chọn ứng dụng để mở
os.startfile(file_2)
# print (m_file.name)