import pandas as pd
import numpy as np

# data_path = r'D:\Study\15.Python\Pandas\excel_file\CMS-Pipe-Test.xlsm'

def create_joint_data(path):
    # import pandas as pd
    # import numpy as np
    df = pd.read_excel(path, sheet_name=0,skiprows=5,
    dtype='str', usecols=[1,7,8,10,11,14,15,18,19,21])
    df['joint_id']=df['Spool No.']+'\\'+df['Dwg. No.']+'\\'+df['Joint No.']+'\\'+df['DB']
    # df=df.fillna(2021)
    df['DB']=df['DB'].astype('float')
    return df

# mdf = create_joint_data(data_path)