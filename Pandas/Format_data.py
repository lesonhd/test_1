# %%
import pandas as pd
import numpy as np

mPath = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-7000-4535.xlsx'
# dùng dtype = 'str' để chuyển cả bảng dữ liệu về dạng text
df = pd.read_excel(mPath, sheet_name=0, skipfooter=5, skiprows=16, usecols=range(1,10),dtype='str')

#  Loại bỏ các dòng có toàn bộ là NaN
df = df.dropna(how='all')
# Chuyển chỗ NaN thành
df = df.fillna(0)
#  Đổi lại số index
df = df.reset_index(drop = True)

#  Chuyển lại cột DB thành dạng số
df['DB'] = df['DB'].astype('float')



print(df)


# df.to_excel('test_2.xlsx')
# print(df)