#  Mở workbook theo đường link thêm chữ r vào trước đường link là được
from openpyxl import load_workbook
import openpyxl

my_file = r'D:/Study/15.Python/openpyxl/Excel_file/1.Fit_up_form.xlsx'
wb = load_workbook(my_file)
ws = wb['FIN']
my_vl = ws['W8'].value

print ( my_vl)

