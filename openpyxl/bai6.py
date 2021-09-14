#  nối và bỏ nối các ô với nhau
from openpyxl import Workbook
from openpyxl import load_workbook
import openpyxl

wb = Workbook()
ws = wb.active
ws.title = 'Sheet-1'
# Nối các ô với nhau
ws.merge_cells('A1:D1')

# Bỏ nối ô với nhau
ws.unmerge_cells('A1:D1')


wb.save('D:/Study/15.Python/openpyxl/Excel_file/file6_merge_cell.xlsx')