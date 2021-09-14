import pandas as pd
import numpy as np

mPath = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-7000-4535.xlsx'
df = pd.read_excel(mPath, sheet_name=0, skiprows= 16, skipfooter=5, usecols=range(1,10))

#  Lọc bỏ các dòng có giá trị Na
df1 = df.dropna(how = 'all')

#  Lọc theo 1 điều kiện
df2 = df.loc[df['Rev.']==1]

# Lọc theo 2 hoặc nhiều điều kiện
df3 = df.loc[(df['Rev.']==1) & (df['Sheet']=='3/5')]

# Lọc theo điều kiện 'Hoặc' - sử dụng dấu | (lọc trong cùng cột dấu | tương đương với và)
df4 = df.loc[(df['Sheet']=='3/5') | (df['Sheet']=='4/5')]

# Lọc theo điều kiện 'Hoặc' - sử dụng dấu | (lọc khác cột dấu | tương đương với 'Hoặc')
df5 = df.loc[(df['Sheet']=='3/5') | (df['Sheet']=='4/5') | (df['Spool No.']=='7000-00600')]

#  reset lại index cho drop = True để không tạo thêm cột index mới mà sửa luôn từ cột index cũ
df5 = df5.reset_index(drop = True)

# Lọc theo điều kiện bao gồm 1 đoạn ký tự
df6 = df.loc[df['Iso. Dwg. No.'].str.contains('NG')]

# Lọc theo điều kiện không bao gồm 1 đoạn ký tự ( thêm dấu ~ vào đầu điều kiện)

df6 = df.loc[~df['Iso. Dwg. No.'].str.contains('NG')]