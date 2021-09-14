# tính giai thừa của một số
# mọi thứ nhập vào bằng hàm input đều là dạng chuỗi, nên phải dùng hàm int để chuyển sang dạng số nguyên
x = int(input('nhập vào một số'))
# sử dụng thuật toán đệ quy để tính giai thừa

def giai_thua(x):
    if x ==0:
        return 1
    else:            
        return x * giai_thua(x-1)
print(giai_thua(x))