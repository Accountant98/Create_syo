import pandas as pd
import streamlit as st

def get_data(sheet_name):
    # Thay đổi để lấy dữ liệu từ sheet_name, ví dụ:
    # df = pd.read_excel('file.xlsx', sheet_name=sheet_name)
    # return df
    # Đây chỉ là một ví dụ placeholder. Bạn nên thay đổi nó để phù hợp với cách bạn lấy dữ liệu.
    return pd.DataFrame({
        'cột1': ['データ1', 'データ2'],
        'cột2': ['データ3', 'データ4']
    })

project_name = "tên_project"  # Thay đổi cho phù hợp với tên project của bạn

st.download_button(
    label="Download File",
    data=get_data(f"仕様表").to_csv(index=False, header=True, encoding='utf-8-sig'),
    file_name=f"仕様表_{project_name.upper()}.csv",
    mime="text/csv",
    use_container_width=True,
)
