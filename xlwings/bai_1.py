import xlwings as xw

def SayHello():
    wb = xw.Book.caller()
    wb.sheets['Sheet1'].range('A1').value = 'Hello World'