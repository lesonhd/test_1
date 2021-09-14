# Điền dữ liệu vào workbook đã được lưu trước đó
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

my_wb = load_workbook('file4.xlsx')

my_ws = my_wb['Sheet']

my_ws['A4'] = 'Dien them2'

j = 2
for i in range(1,5):
    my_ws.cell(i,j, value= i+j)


my_wb.save('file4.xlsx')

