import pandas as pd
import numpy as np

# Tạo dữ liệu mẫu cho result_df_matched
data_result = {
    'cadic_number': ['123', '456', '789', '101', '102', '103', '104'],
    'value': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'note_1': ['note1', 'note2', 'note3', 'note4', 'note5', 'note6', 'note7'],
    'note_2': ['note8', 'note9', 'note10', 'note11', 'note12', 'note13', 'note14'],
    'col1': ['val1', 'val2', 'val3', 'val4', 'val5', 'val6', 'val7'],
    'col2': ['val8', 'val9', 'val10', 'val11', 'val12', 'val13', 'val14'],
    'col3': ['val15', 'val16', 'val17', 'val18', 'val19', 'val20', 'val21']
}
result_df_matched = pd.DataFrame(data_result)

# Tạo dữ liệu mẫu cho data_edit
data_edit = {
    'cadic_number': ['123', '456', '789', '101', '102', '103', '105'],
    'value': ['A', 'B', 'C', 'D', 'E', 'F', 'H'],
    'note_1': ['note1', 'note2', 'note3', 'note4', 'note5', 'note6', 'note8'],
    'note_2': ['note8', 'note9', 'note10', 'note11', 'note12', 'note13', 'note15'],
    'col1': ['val1', 'val2', 'val3', 'val4', 'val5', 'val6', 'val8'],
    'col2': ['val8', 'val9', 'val10', 'val11', 'val12', 'val13', 'val15'],
    'col3': ['val15', 'val16', 'val17', 'val18', 'val19', 'val20', 'val22']
}
data_edit = pd.DataFrame(data_edit)

# Giả sử id_project và id_app_list là như sau
id_project = 1
id_app_list = [1, 2, 3]


def update_edit(data_edit, result_df_matched, id_project, id_app_list):
    try:
        columns = [col for col in result_df_matched.columns if
                   col not in ['id', 'id_project', 'id_app', 'value', 'note_1', 'note_2']]

        result_df_matched.replace({np.nan: ''}, inplace=True)
        data_edit.replace({np.nan: ''}, inplace=True)
        data_edit.columns = result_df_matched.columns

        main_table_df_1 = result_df_matched.iloc[6:]
        main_table_df_2 = data_edit.iloc[6:]

        merged = pd.merge(main_table_df_1, main_table_df_2, indicator=True, how='outer')
        different = merged[merged['_merge'] == 'left_only']
        cadic_number_insert_or_update = tuple(different.iloc[:, 0].to_list())

        different = merged[merged['_merge'] == 'right_only']
        different = different.drop(different.columns[-1], axis=1)
        different = different.reset_index(drop=True)
        different = different.values.tolist()

        characters_to_omit = "<>'\"!$%^&[]"
        translation_table = str.maketrans("", "", characters_to_omit)
        different = [
            [s.translate(translation_table) if isinstance(s, str) else '' for s in sublist]
            for sublist in different
        ]

        if different:
            main_table_objects = []
            for item in different:
                note_1_idx = 4 + len(id_app_list)
                note_2_idx = 5 + len(id_app_list)
                if note_1_idx < len(item) and note_2_idx < len(item):
                    note_1 = str(item[note_1_idx])
                    note_2 = str(item[note_2_idx])

                    for app in id_app_list:
                        app_idx = 4 + id_app_list.index(app)
                        if app_idx < len(item):
                            config_value = str(item[app_idx])
                            main_table_objects.append(
                                {'id_project': id_project, 'id_app': app, 'value': config_value, 'note_1': note_1,
                                 'note_2': note_2,
                                 **{col: value for col, value in zip(columns, item)}})

            # Do something with main_table_objects
            print("Main Table Objects:", main_table_objects)

        header_df_new_list = data_edit.iloc[:6, :].values.tolist()
        header_df_old_list = result_df_matched.iloc[:6, :].values.tolist()
        set_header_old = set(map(tuple, header_df_old_list))
        set_header_new = set(map(tuple, header_df_new_list))
        header_different_set = set_header_new - set_header_old
        header_different_list = list(map(list, header_different_set))

        if header_different_list:
            header_different_list = [
                [s.translate(translation_table) if isinstance(s, str) else '' for s in sublist]
                for sublist in header_different_list
            ]
            # Do something with header_different_list
            print("Header Different List:", header_different_list)

        chars_to_replace = ['<', '>', "'", '"', '!', '#', '$', '%', '^', '&', '[', ']']
        for col in data_edit.columns:
            for char in chars_to_replace:
                data_edit[col] = data_edit[col].str.replace(char, '')

        return data_edit

    except Exception as e:
        print(f"Error saving changes: {e}")


# Gọi hàm với dữ liệu mẫu
updated_data_edit = update_edit(data_edit, result_df_matched, id_project, id_app_list)
print("data_edit: ", data_edit)
print("result_df_matched: ", result_df_matched)
# Xem kết quả
print("updated_data_edit: ", updated_data_edit)
