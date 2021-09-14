# Điền dữ liệu
from openpyxl import Workbook
import openpyxl
wb = Workbook()
ws = wb.active

#  Điền dữ liệu vào ô A1
ws['A1'] = 'CLGT'
#  Điền dữ liệu vào ô A2
ws.cell(row=2,column=1,value='Điền dữ liệu vào ô A2')
# Điền dữ liệu vào ô A3
ws.cell(3,1,'Điền dữ liệu vào ô A3')

#  In dữ liệu của ô A1
print (ws['A1'].value)

#  Lấy dữ liệu từ ô A1 Sang ô C1
ws['C1'] = ws['A1'].value

# Duyệt qua các ô từ A1 đến A3
j = 1
for i in range(1,4):
    print(ws.cell(i,j).value)

wb.save('File2.xlsx')
