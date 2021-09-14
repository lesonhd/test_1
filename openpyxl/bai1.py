from openpyxl import Workbook
# Tạo workbook
wb = Workbook()
# Sheet được tạo ra đầu tiên là sheet active
ws = wb.active
#  Đặt tên mới cho sheet đầu tiên
ws.title = 'Sheet dau tien duoc tao ra'
#  Thêm 1 sheet mới, với vị trí là số 1 ( trong python sheet0 là sheet đầu tiên)
ws1 = wb.create_sheet('Date_time',1)
# Đổi màu cho sheet
ws.sheet_properties.tabColor = '1072BA'
# in ra danh sách các sheet ( Danh sách các sheet trong wb.sheetnames là 1 list)
print(wb.sheetnames)
#  lặp qua các sheet
for mySheet in wb:
	print(mySheet.title)
# Copy worksheet
ws2 = wb.copy_worksheet(ws)
#  Lưu thành 1 file
wb.save('file1.xlsx')
