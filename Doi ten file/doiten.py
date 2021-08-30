import pandas as pd
import numpy as np
import os

# mpath = 'D:\\Study\\15.Python\\ten_file.xlsx'
# mwb = pd.ExcelFile(mpath)

df = pd.read_excel('ten_file.xlsx')
dic_ten_file = pd.DataFrame.to_dict(df)
ten_nguon = list(dic_ten_file['Ten_nguon'].values())
ten_moi = list(dic_ten_file['Ten_moi'].values())

# print(ten_moi)
# print(ten_nguon)

# #  tạo list là danh sách trích từ file excel tên cũ của các file
# df1 = pd.read_excel(mwb, usecols=[0])
# dic_nguon = pd.DataFrame.to_dict(df1)
# ten_nguon = list(dic_nguon['Ten_nguon'].values())

# # #  tạo list là danh sách trích từ file excel tên mới của các file
# df2 = pd.read_excel(mwb,usecols=[1])
# dic_moi = pd.DataFrame.to_dict(df2)
# ten_moi = list(dic_moi['Ten_moi'].values())

# print(ten_moi)

#  đổi tên file
for i in range(len(ten_nguon)):
    os.rename(ten_nguon[i],ten_moi[i])

