#pip3 install openpyxl
import openpyxl

#specify the files location (or path)
excel_files = ['/Users/vishnupriya/Downloads/Excel_Automation/datasets/SampleData2.xlsx']

#loop through the files in the "excel_files" list
for file in excel_files:
    wb = openpyxl.load_workbook(file)
    #locate worksheet
    worksheet = wb["SalesOrders"]
    #compute average in G46
    worksheet['G48'] = '=AVERAGE(G3:G45)'
    #save the file
    wb.save(file)
print('Done,Check the Excel Sheet now!')
    