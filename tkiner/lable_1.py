from tkinter import *


list_update = [1,2,4,'f','f','s']
list_trung = ['d','f','j']
list_ko_update  = [1,2]


m_string_2 = ('Số mối đã được update: %s\nSố mối bị trùng: %s\nSố mối không update được: %s\n' 
    %(len(list_update),len(list_trung),len(list_ko_update)))

Root = Tk()
Root.title('Update Status')
Root.geometry('300x70')

m_label = Label(Root, text = m_string_2)
m_label.pack()

mainloop()
