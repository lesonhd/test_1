# Công thức tạo ra dataframe của các file excel fit-up visual
#  Biến truyền vào là đường dẫn
# kết quả trả về là 1 dataframe đã được "làm sạch"
import pandas as pd
import numpy as np

mPath1 = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-7000-4535.xlsx'
mPath2 = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-1000-4534.xlsx'

path_list = [mPath1,mPath2]
def Creat_df(path):
    df = pd.read_excel(path, sheet_name=0, usecols=range(1,10), 
    skipfooter=5, skiprows=16, dtype='str')
    df = df.dropna(how ='all')
    df = df.fillna(0)
    df = df.reset_index(drop = True)
    df['DB'] = df['DB'].astype('float')
    df['joint_id'] = df['Spool No.']+'\\'+df['Iso. Dwg. No.']+'\\'+df['Joint No.']
    
    return df
mdf = []
for path in path_list:
    df = Creat_df(path)
    mdf.append(df)


