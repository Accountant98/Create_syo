import pandas as pd


def check_optioncode_from_syo(df):
    opt_index = df.index[df['CADICS ID'] == 'OptionCode'].values[0]
    conf_columns = ['CADICS ID'] + [col for col in df.columns if col.startswith('conf-')]
    df_end = df.loc[opt_index:, conf_columns]
    first_row = df_end.iloc[0]
    contains_non_nan = first_row[conf_columns].notna().any()
    return contains_non_nan


if __name__ == '__main__':
    file_path = r"C:\Users\KNT21617\Downloads\newken\仕様表\仕様表_PZ1K_copy - Copy.xlsx"
    df = pd.read_excel(file_path)
    results = check_optioncode_from_syo(df)
    print(results)
