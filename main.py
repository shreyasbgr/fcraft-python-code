from calendar import c
import pandas as pd
def get_all_errors(file):
    df = pd.read_csv(file)
    for ind in df.index:
        for col in df.columns:
            if col == 'PNR':
                if len(df[col][ind])!=6:
                    print(f"Row {ind+1} PNR is wrong.",end =' ')    
            elif col == 'Invoice Number':
                if len(df[col][ind])>16:
                    print(f"Row {ind+1} Invoice no. is wrong.",end =' ')
            elif col == 'GST Amount':
                if  not isinstance(df[col][ind],int) and not isinstance(df[col][ind],float):
                    print(f"Row {ind+1} GST Amount is wrong.",end =' ')
            


if __name__=='__main__':
    get_all_errors('csv_files/sample.csv')