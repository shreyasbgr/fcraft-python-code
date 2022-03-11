from datetime import datetime
import numpy as np
import pandas as pd
def get_all_errors(file):
    df = pd.read_csv(file)
    df['CONCAT of PNR&Invoice Number']=df['PNR']+df['Invoice Number']
    df['GST Amount'] = pd.to_numeric(df['GST Amount'], errors='coerce')
    dict_concat_pnr_invoice ={}
    for ind in df.index:
        for col in df.columns:
            if col == 'PNR':
                if len(df[col][ind])!=6:
                    print(f"Row {ind+2} Col name {col} - PNR is not equal to 6 characters.")    
            elif col == 'Invoice Number':
                if len(df[col][ind])>16:
                    print(f"Row {ind+2} Col name {col} - Invoice no. is greater than 16 characters.")
            elif col == 'GST Amount':
                if np.isnan(df[col][ind]):
                    print(f"Row {ind+2} Col name {col} - GST Amount is not a number.")
            elif col == 'Invoice date':
                current_date=datetime.now()
                given_date=datetime.strptime(df[col][ind], "%d-%b-%y")
                if given_date > current_date:
                    print(f"Row {ind+2} Col name {col} - Invoice date is greater than the current date.")
            elif col == 'Customer GSTIN':
                if len(df[col][ind])!=15:
                    print(f"Row {ind+2} Col name {col} - Customer GSTIN is not equal to 15 characters.")
            elif col == 'CONCAT of PNR&Invoice Number':
                if df[col][ind] in dict_concat_pnr_invoice:
                    print(f"Row {ind+2} Col name {col} - CONCAT of PNR&Invoice Number cannot be duplicate.")
                else:
                    dict_concat_pnr_invoice[df[col][ind]]=True
    
    df.to_csv('csv_files/processed_sample.csv',index=False)
if __name__=='__main__':
    get_all_errors('csv_files/sample.csv')