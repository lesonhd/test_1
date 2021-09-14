import openpyxl
from openpyxl import load_workbook
m_path = r'E:\Onedrive\9.Packet A1\9.QA-QC-WE\12.Form\25_W24 Form.xlsx'
wb = load_workbook(m_path)
ws = wb.worksheets[0]

ws.cell(9,2).value = 'khoahoc 10202'
# ws.cell(2,1).value = 'khoahocdfsdf 10202'
ws.cell(11,3).value = 'sdjfksjdlfks'
wb.save('Write_merged_cell_1.xlsx')
wb.close
