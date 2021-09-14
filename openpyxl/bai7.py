# ẩn hiện dòng cột
from openpyxl import Workbook
import openpyxl

wb = Workbook()
ws = wb.active
ws.title = 'Bai 7'

ws.column_dimensions.group('A','D', hidden=True)

# ws.PAPERSIZE_A4

wb.save('D:/Study/15.Python/openpyxl/Excel_file/file7_hiden.xlsx')
