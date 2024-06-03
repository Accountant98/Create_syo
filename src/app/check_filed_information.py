import win32com.client
import pandas as pd
import re
import os


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


def get_xlsx_files(directory_path):
    xlsx_files = [filename for filename in os.listdir(directory_path) if filename.endswith('.xlsx')]
    xlsx_paths = [os.path.join(directory_path, filename) for filename in xlsx_files]
    return xlsx_files, xlsx_paths


def check_key_spec():
    directory_path = os.path.abspath(os.path.join(os.getcwd(), "../../data/raw"))
    xlsx_files, xlsx_paths = get_xlsx_files(directory_path)
    list_key_check_row_15 = ['Class', 'Attributes', 'Option Package', 'ZONE', 'BODY']
    list_end = []
    for file_name, file_path in zip(xlsx_files, xlsx_paths):
        sheet_name = 2
        print("file_path: ", file_path)
        print("sheet_name: ", sheet_name)
        df = read_protected_excel(file_path, sheet_name)
        list_key_word_1 = df.iloc[14].tolist()
        name_column = df.iloc[14].eq('NAME').idxmax()
        list_key_word_2 = df.iloc[:, name_column].tolist()
        list_key_word = list_key_word_1 + list_key_word_2
        dict_sub = {'file_name': None, 'Class': None, 'Attributes': None, 'Option Package': None, 'ZONE': None,
                    'BODY': None}
        for item in list_key_check_row_15:
            if item not in list_key_word:
                if dict_sub['file_name'] is None:
                    dict_sub['file_name'] = file_name
                dict_sub[item] = '✕'
        if list(set(dict_sub.values())) != [None]:
            list_end.append(dict_sub)
    df = pd.DataFrame(list_end)
    return df


if __name__ == "__main__":
    x = check_key_spec()
    print(x)
