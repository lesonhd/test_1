import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

wb = Workbook()
ws =wb.active

mdic = {'a1':[1,2,2,4,5],
        'A2':[123,231,3,4,8]}

df = pd.DataFrame(mdic)
# rows = dataframe_to_rows(df,index=True, header = True)
for r in dataframe_to_rows(df,index=True, header = True):
    ws.append(r)

wb.save('df_to_excel.xlsx')
wb.close()