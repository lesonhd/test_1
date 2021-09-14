import openpyxl
from openpyxl import load_workbook

wb = load_workbook('df_to_excel.xlsx')
ws = wb.worksheets[0]
print(wb.sheetnames)