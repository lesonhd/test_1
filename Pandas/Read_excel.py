import pandas as pd
import numpy as np

mPath = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-7000-4535.xlsx'

#  dtype để định dạng lại cho cột (chọn str để chuyển toàn bộ sang text)
df = pd.read_excel(mPath, sheet_name=0, usecols=range(0,10),
    skipfooter=5,skiprows= 16, dtype='str'')

# Xóa bỏ dòng Na
df = df.dropna(how = 'all')
#  thay dữ liệu Na thành 0
df = df.fillna(0)
#  reset  lại cột index
df = df.reset_index(drop = True)



