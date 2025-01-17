import numpy as np
import streamlit
import win32com.client
import pandas as pd
import re
import os
import math


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
        # print("file_path: ", file_path)
        # print("sheet_name: ", sheet_name)
        # df = read_protected_excel(file_path, sheet_name)
        df = pd.read_excel(file_name, header=False, sheet_name=1)
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


def check_key_spec_new(file_name):
    flg_check_fail = False
    list_key_check_row_15 = ['Class', 'Attributes', 'Option Package', 'ZONE', 'BODY', 'ENGINE', 'AXLE', 'HANDLE',
                             'GRADE', 'TRANS', 'YEAR', 'INTAKE', 'SEAT/EQUIP', 'NUMBER']
    list_end = []
    dict_sub = {'file_name': None, 'Class': None, 'Attributes': None, 'Option Package': None, 'ZONE': None,
                'BODY': None, 'ENGINE': None, 'AXLE': None, 'HANDLE': None,
                'GRADE': None, 'TRANS': None, 'YEAR': None, 'INTAKE': None, 'SEAT/EQUIP': None, 'NUMBER': None,
                'SHEET_NAME': None}
    try:
        df = pd.read_excel(file_name, header=None, sheet_name='1-SPEC')
    except:
        dict_sub['file_name'] = file_name.name
        dict_sub['SHEET_NAME'] = '✕'
        flg_check_fail = True
        df = pd.DataFrame([dict_sub])
        streamlit.write(df)
        return df, flg_check_fail

    list_key_word_1 = df.iloc[14].tolist()
    list_key_word_1_processed = [x for x in list_key_word_1 if not (isinstance(x, float) and math.isnan(x))]
    name_column = df.iloc[14].eq('NAME').idxmax()
    list_key_word_2 = df.iloc[:, name_column].tolist()
    list_key_word_2_processed = [x for x in list_key_word_2 if not (isinstance(x, float) and math.isnan(x))]
    list_key_word = list_key_word_1_processed + list_key_word_2_processed

    for item in list_key_check_row_15:
        if item not in list_key_word:
            if dict_sub['file_name'] is None:
                dict_sub['file_name'] = file_name.name
            dict_sub[item] = '✕'
    if list(set(dict_sub.values())) != [None]:
        list_end.append(dict_sub)
    df = pd.DataFrame(list_end)

    if not df.empty:
        flg_check_fail = True
    return df, flg_check_fail


def check_syo(df_):
    list_error = []
    for item in ['auto', 'Gr', 'Keyword', 'CADICS ID']:
        if item not in df_.columns:
            list_error.append(item)
    columns_with_missing_values = df_.columns[df_.isna().all()].tolist()
    filtered_list = [item for item in columns_with_missing_values if not item.startswith('comment_')]
    if filtered_list:
        print('columns_with_missing_values: ', columns_with_missing_values)
        return ['Columns with missing values'], []
    required_columns = ['Gr', 'Keyword', 'CADICS ID', 'auto']
    missing_columns = [col for col in required_columns if col not in df_.columns]
    if missing_columns:
        return ['(Gr, Keyword, CADICS ID, AUTO) columns not in data'], []
    df_['CADICS ID'] = df_['CADICS ID'].str.strip()
    valid_df = df_[df_['CADICS ID'].notna() & (df_['CADICS ID'] != '')]
    duplicated_elements_ = valid_df[valid_df.duplicated('CADICS ID', keep=False)]['CADICS ID'].unique().tolist()
    # print('list_error: ', list_error)
    # print('duplicated_elements_: ', duplicated_elements_)
    return list_error, duplicated_elements_


def check_optioncode(df_):
    conf_columns = [col for col in df_.columns if col.startswith('conf-')]
    df_ = df_.replace('', None)
    rows_with_cadic = df_[df_['CADICS ID'] == 'OptionCode']
    for index, row in rows_with_cadic.iterrows():

        if row[conf_columns].isna().all():
            return True
        else:
            return False

#
# if __name__ == "__main__":
#     df = pd.read_excel(r"C:\Users\KNT21617\Downloads\newken\project\data\input_syo\CAR 1.xlsx")
#     print(df['CADICS ID'])
#     list_error, duplicated_elements = check_syo(df)
#     print(list_error, duplicated_elements)
