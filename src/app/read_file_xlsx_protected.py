import os

import win32com.client
import pandas as pd
import re


def read_protected_excel(file_path_, sheet_name_):
    # Extract the password from the file name
    name = file_path_.split('\\')
    text = name[-1]
    match = re.search(r'\((.*?)\)', text)
    password_ = match.group(1)

    # Initialize the Excel Application object
    xlApp = win32com.client.Dispatch("Excel.Application")

    # Open the Excel file and authenticate with the password
    xlwb = xlApp.Workbooks.Open(file_path_, False, True, None, password_)

    xlApp.Visible = False
    xlwb.Worksheets(sheet_name_).Activate()
    readData = xlwb.Worksheets(sheet_name_)
    ws = xlwb.ActiveSheet

    # Get data from the sheet
    allData = readData.UsedRange
    EndRow = allData.Rows.Count
    EndCol = allData.Columns.Count

    # Retrieve the content of the sheet and convert it to a DataFrame
    content = ws.Range(ws.Cells(1, 1), ws.Cells(EndRow, EndCol)).Value
    df = pd.DataFrame(list(content))

    xlwb.Close(False)
    return df


# file_path = os.path.join(os.getcwd(), r"..\..\data\raw\(pz1k)PZ1K_0-Phase_Spec_List_sq1 のコピー のコピー.xlsx")
# file_path = r"C:\Users\KNT21617\Downloads\newken\project\data\raw\(wz1j)WZ1J_Advanced_Spec_List_sq2 のコピー.xlsx"
# sheet_name = 2
# df = read_protected_excel(file_path, sheet_name)
# print(df)



