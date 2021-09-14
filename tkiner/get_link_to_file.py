from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os

Root_tk = Tk()
mFolder = filedialog.askdirectory(title='Chọn Folder update Fit-up')

m_Files = []
for links, folders, files in os.walk(mFolder):
    for file in files:
            f = os.path.join(links,file) # dùng extend thì thêm [], dùng append thì ko cần
            m_Files.append(f)

print(m_Files)
# Root_tk.mainloop()