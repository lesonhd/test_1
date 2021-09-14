def my_func():
    my_range = []
    for my_num in range(2000,3201):
        if my_num % 7 == 0 and my_num % 5 != 0:
            my_range.append(str(my_num))
#  hàm jont để nối dấu ',' vào list
    print(','.join(my_range))
my_func()
