import pandas as pd
import numpy as np
from openpyxl import load_workbook

#  Đặt đường dẫn đến các file FU và file data

mpath2 = r'D:\Study\15.Python\Pandas\excel_file\FU-WEC-C-7000-4535.xlsx'


data_path = r'D:\Study\15.Python\Pandas\excel_file\CMS-Pipe-Test.xlsm'

# Chèn module đã tạo vào trong scrip
from module_update import fu_report, fu_data
report_df = fu_report.create_fu_data(mpath2)

date_rp = fu_report.list_date_report(mpath2)
report_no = fu_report.list_report_no(mpath2)


# tạo dataframe cho joint data
data_df = fu_data.create_joint_data(data_path)

# So sánh data và nhặt ra được list bị trùng, list ko update được, list sẽ update
def compare_fun(report_dataFrame,data_dataFrame):
    joint_bc=[]
    joint_trung=[]
    joint_koupdate = []
    for i in report_dataFrame['joint_id'].index:
        data_df_ss= data_dataFrame[data_dataFrame['joint_id']==report_dataFrame['joint_id'][i]]
        # So sánh joint id và DB
        if ((len(data_df_ss.index)!=0) & 
            (report_dataFrame['DB'][i]==data_df_ss['DB'][data_df_ss['joint_id'].index[0]])):
            # Nếu đúng --> ô report có phải ô trống không
            if pd.isna(data_df_ss['Report_FU'][data_df_ss['joint_id'].index[0]]):
                # Nếu đúng thêm joint vào list joint sẽ được update
                joint_bc.append(data_df_ss['joint_id'].index[0])
            else:
                # Nếu sai thêm váo list mối bị trùng
                joint_trung.append(data_df_ss['joint_id'].index[0])
        else:
            # Nếu Sai them vào list không update được
            joint_koupdate.append(i)
    return joint_bc, joint_trung, joint_koupdate

compare_result = compare_fun(report_df,data_df)

# In list bị trùng ra 1 file.
if len(compare_result[2])!=0:
    df_trung=data_df.filter(items=joint_trung, axis=0)
    df_trung.to_excel('joint_fit-up_trung.xlsx')
    
# In list khong update được ra 1 file
if len(compare_result[3])!=0:
    df_koupdate = report_df.filter(items=joint_koupdate, axis=0)
    df_koupdate.to_excel('ko_update.xlsx')

