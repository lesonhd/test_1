import pandas as pd
import numpy as np
from openpyxl import load_workbook
from datetime import date

m_rp = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-7000-4535.xlsx'

# Lấy df số báo cáo
rp_num_df = pd.read_excel(m_rp,usecols='I', skiprows=5, header=0)
rp_num_df = rp_num_df.filter(items=[0], axis=0)
# Lấy df ngày báo cáo
rp_date_df = pd.read_excel(m_rp,usecols='E', skiprows=13, header=0)
rp_date_df = rp_date_df.filter(items=[0], axis=0)

# Viết vào file test
m_list = [1,2,5,7]
m_data = r'D:\Study\15.Python\Pandas\test.xlsm'
# 
# Dùng openpyxl viết thêm vào file là dễ nhất
for i in m_list:
    with pd.ExcelWriter(m_data, mode='a', engine='openpyxl') as writer:
        rp_num_df.to_excel(writer, header=False, index= False, startcol=7, startrow=i, sheet_name='Sheet1')