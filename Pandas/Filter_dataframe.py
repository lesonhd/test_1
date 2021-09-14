import pandas as pd
import numpy as np

mpath = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-7000-4535.xlsx'

df = pd.read_excel(mpath, sheet_name=0,usecols=range(1,10),dtype='str',
    skipfooter=5, skiprows=16)
df = df.dropna(how='all')
df = df.fillna(0)
df = df.reset_index(drop=True)
df['DB']=df['DB'].astype('float')
# Lệnh filter để lọc theo tên cột hoặc tên hàng.
# Biến items để điền các tiêu đề muốn lọc ra, biến axis =1 là lọc theo cột, =0 là theo hàng
# 
# lọc theo cột
df1 = df.filter(items=['Sheet','Rev.','Size'], axis=1)

#  lọc theo hàng
df3 = df.filter(items=[0,1,3,7], axis=0)

# Sử dụng biến regex và like để lọc theo ký tự
# lọc các cột có chứa Sh
df4 = df.filter(regex="Sh", axis=1)
# lọc các cột có kết thúc bằng t
df5 = df.filter(regex ='t$', axis = 1)

# lọc các cột có chứa o
df6 = df.filter(like='o', axis=1)

# Lọc giá trị của data không sử dụng loc
df7 = df[df['DB']>10]   # lọc 1 điều kiện
df8 = df[(df['DB']>5) & (df['Rev.']=='1A')] # lọc 2 điều kiện
df9 = df[(df['Rev.']=='1A') | (df['DB']==16)] # lọc vơi điều kiện hoặc

# Lọc sử dụng isin
df10 = df[df['DB'].isin([16,5])]

# Lọc sử dụng query
df11 = df.query('Sheet==["3/5","1/2"]')