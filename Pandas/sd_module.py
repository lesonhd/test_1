import pandas as pd
import numpy as np

# Chèn module đã tạo vào trong scrip
# from module_update import fu_report
from module_update import *


mpath1 = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-1000-4534.xlsx'
mpath2 = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-7000-4535.xlsx'
mpath = [mpath1,mpath2]

fu_df = []
for path in mpath:
    df = fu_report.create_fu_data(path)
    fu_df.append(df)


# from module_update import fu_data
data_path = r'D:\Study\15.Python\Pandas\excel_file\CMS-Pipe-Test.xlsm'

data_df = fu_data.create_joint_data(data_path)