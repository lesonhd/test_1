import xlwings as xw
import pandas as pd


m_dic = {'spool_No':['0100-0001','0100-0002','0100-0003','0100-0004'],
        'Length':[120,1253,1630,1564]}

df = pd.DataFrame(m_dic)

# thêm một dấu () nữa nó mới chạy
wb = xw.Book((r'D:\Study\15.Python\form_2.xlsx'))
wb.sheets[0].range('B2').value = df
wb.save()
wb.close()

