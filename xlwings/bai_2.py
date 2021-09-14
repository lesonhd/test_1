import pandas as pd
import numpy as np
import xlwings as xw

m_df = pd.DataFrame({'A': [1,2,3,4], 'B': [6,7,8,9]})
# #  chuyển từ dataframe sang dict sử dụng orient là split sẽ tách ra thành key seri, ky data, key colum
m_dic = m_df.to_dict('split')
m_dic2 = m_dic['data']
def dienreport():
    wb = xw.Book.caller()
    wb.sheets[0].range('B2').value = m_dic2
    

