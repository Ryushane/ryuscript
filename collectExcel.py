import os
os.chdir(r'C:/Users/Ryushane/Desktop/resdata')
import glob
import pandas as pd

paths = glob.glob('*.xlsx')
print(paths,'\n')
print('------------\n')
df = pd.DataFrame()
for path in paths:
    df_ = pd.read_excel(path)
    df = pd.concat([df,df_])

print(len(df))
df.to_excel('data.xlsx',index = False)
