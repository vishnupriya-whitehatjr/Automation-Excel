#pip3 install pandas
#pip install xlrd==1.2.0
import pandas as pd

#specify the files location (or path)
excel_files = ['datasets/SampleData.xlsx']

#create a blank dataframe
merge = pd.DataFrame()

#loop through every file in the list
for file in excel_files:
  #read files into a dataframe and skip the first row (header)
  df = pd.read_excel(file, skiprows = 1)
  #append results to merge
  merge = merge.append(df, ignore_index = True)

#create final workbook with merged results
merge.to_excel('datasets/Merged_Files.xlsx')
print("Done!")
