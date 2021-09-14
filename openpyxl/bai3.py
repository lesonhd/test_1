# Chèn công thức vào bảng tính:
from openpyxl import Workbook
import openpyxl

wb = Workbook()
ws = wb.active
ws.title = 'Bai 3'

ws['A1'] = 10
ws['A2'] = ws['A1'].value + 12
ws['C1'] = '=Sum(A1:A2)'

wb.save('file3_congThuc.xlsx')
