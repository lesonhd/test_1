import os
# Tạo folder
# os.makedirs('test_folder')    

# #xóa folder
# os.rmdir('test_folder')

# #Xóa file
# os.remove('1_2.TXT')                

# Đổi tên file
# os.rename('234.TXT', '678.TXT')

# Mở file
# os.startfile('678.TXT')

mPath = r'D:\Study\15.Python\test_1\OS_module\678.TXT'

# Lấy tên file
# os.path.basename(mPath)

# Lấy tên dường dẫn thư mục chưa file
# os.path.dirname(mPath)

# Kiểm tra file hoặc đường dẫn có tồn tại hay không
# os.path.exists(mPath)

# Kiểm tra xem có phải là file ko
# os.path.isfile(mPath)

# Kiểm tra xem có phải đường dẫn không
# os.path.isdir(mPath)

# Tách đường dẫn
mPath1 = os.path.split(mPath)
mPath1

# Nnối đường dẫn
mPath_2 = os.path.join(mPath1[0],mPath1[1])

