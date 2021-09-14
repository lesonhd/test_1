import openpyxl
from openpyxl import load_workbook
m_paht = r'D:\Study\15.Python\openpyxl\file2.xlsx'
wb = load_workbook(m_paht, read_only=False)
ws = wb.worksheets[0]
for i in range(2,12):
    ws.row_dimensions[i].hidden = True
# ws.column_dimensions['A'].hidden = True
wb.save(m_paht)

wb.close()