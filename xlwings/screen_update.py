import xlwings as xw

app = xw.apps.active
app.visible = False
app.screen_updating = False
app.display_alerts = False

m_wb = xw.Book()
m_wb.sheets[0].name = '123'


app.visible = True
app.screen_updating = True
app.display_alerts = True