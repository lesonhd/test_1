# Chèn ảnh vào  file excel
from openpyxl.drawing.image import Image
from openpyxl import Workbook

m_wb = Workbook()
m_ws = m_wb.active
m_ws.title = 'Sheet Moi'

# m_wb.save('file5_logo.xlsx')

m_pic = Image(r'D:/Study/15.Python/openpyxl/Excel_file/pic_1.jpg')

m_ws.add_image(m_pic,'A1')

m_wb.save(r'D:/Study/15.Python/openpyxl/Excel_file/file5_logo.xlsx')