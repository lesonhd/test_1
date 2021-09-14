import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

m_path = r'D:\Study\15.Python\openpyxl\file2.xlsx'
wb = load_workbook(m_path)
ws = wb.worksheets[0]

mdic = {'a1': [1,2,2,4,5],
        'A2': [123,231,3,4,8]}

df = pd.DataFrame(mdic)

# Chuyển từ df sang dạng dữ liệu có thể điền được vào file excel
rows = dataframe_to_rows(df, index= False, header= False)

# Mỗi r trong rows là 1 list theo hàng ngang. từ đó có thể điền vào form có sẵn
i = 2
for r in rows:
    ws.cell(i,2).value = r[0]
    ws.cell(i,3).value = r[1]
    i+=1

wb.save(m_path)
wb.close