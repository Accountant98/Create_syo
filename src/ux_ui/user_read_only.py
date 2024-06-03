import streamlit as st
from streamlit_extras.grid import grid
import io
from .read_data_view import *


def reset_data():
    if st.session_state.get('data') is None:
        st.session_state['data'] = {}


def set_data(key: str, value):
    st.session_state['data'][key] = value


def get_data(key):
    return st.session_state['data'].get(key)


def user_read_only():
    reset_data()
    col_left, col_right = st.columns([1, 3])
    with col_left:
        with st.form('input_form'):
            # PROJECT BOX
            col_left_prj_grid = grid(1, 2, 2, vertical_align="top")
            # Row 1:
            col_left_prj_grid.header("Project")
            # Row 2:
            col_left_prj_grid.text_input("Model Code", key="code")
            col_left_prj_grid.selectbox("PowerTrain", ['EV', 'e-Power', 'ICE'], key="pwt")
            # Row 3:
            col_left_prj_grid.selectbox("Case", ['CASE1', 'CASE1.5', 'CASE2'], key="case")
            col_left_prj_grid.selectbox("Plant", ['JPN', 'US', 'EUR', 'PRC'], key="plant")

            st.header("View Box")
            col_left_spec_grid = grid(1, vertical_align="top")
            if col_left_spec_grid.form_submit_button("View", use_container_width=True):
                # with st.spinner(text="In progress..."):
                #     print()
                #     set_data("flag_view", 1)
                set_data("link", "cadics")
                # st.write("Completed!!!")
            # BANNER RIGHT
            with col_right:
                col_r1, col_r2 = st.columns([2, 1])
                with col_r1:
                    st.markdown(
                        '<h1 style="text-align: center;background-color: #CCE9D9;border: 2px solid #4CAF50; padding: 10px;">仕様表自動作成</h1>',
                        unsafe_allow_html=True)
                with col_r2:
                    st.markdown(
                        f'<p style="text-align: center;">{st.session_state.name_user}<br>{st.session_state.position}</p>',
                        unsafe_allow_html=True)

                view("staff")


def view(position, project_name):
    button_select_caout_grid = grid(1, 1, 1, vertical_align="top")
    row_butt = st.columns(5)

    if get_data("flag_view") == 1:
        button_select_caout_grid.dataframe(get_data("仕様表"), height=710)
        with row_butt[2]:
            if get_data("link") == "cadics":
                css = """
                    <style>
                        .stDownloadButton > button {
                            background-color: rgba(0, 0, 255, 0.5);  /* Màu xanh lam với độ trong suốt 50% */
                            color: white;
                            border: 1px solid black;
                        }
                        .stDownloadButton > button:hover {
                            background-color: darkorange;
                            color: white;
                        }
                    </style>
                """
                st.markdown(css, unsafe_allow_html=True)

                # Tạo DataFrame từ dữ liệu
                df = get_data("仕様表")
                device_group = get_data("device_group")
                device = get_data("device")
                # Tạo một đối tượng BytesIO để lưu file xlsx
                output = io.BytesIO()

                # Ghi DataFrame vào đối tượng BytesIO dưới dạng file xlsx với định dạng
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, header=False, sheet_name='Sheet1')

                    # Lấy workbook và worksheet từ writer
                    workbook = writer.book
                    worksheet = writer.sheets['Sheet1']

                    # Tạo định dạng màu xanh
                    highlight_format_device_group = workbook.add_format({'bg_color': '#535353', 'font_color': '#FFFFFF'})
                    highlight_format_device = workbook.add_format({'bg_color': '#245269', 'font_color': '#FFFFFF'})

                    # Áp dụng định dạng màu vàng cho hàng chứa giá trị 'X01_VISIBILITY' trong cột A
                    for row_num, value in enumerate(df['auto'], start=0):
                        if str(value) is not None:
                            if str(value) in device_group:
                                worksheet.set_row(row_num, None, highlight_format_device_group)
                            if str(value) in device:
                                worksheet.set_row(row_num, None, highlight_format_device)

                # Đặt lại vị trí của con trỏ trong đối tượng BytesIO về đầu
                output.seek(0)

                # Sử dụng st.download_button để tải file xlsx
                st.download_button(
                    label="Download File",
                    data=output,
                    file_name=f"仕様表_{project_name.upper()}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True,
                )

    else:
        data_empty = pd.DataFrame([[""] * 30] * 30)
        column_names = [f'{i + 1}' for i in range(30)]
        data_empty = pd.DataFrame(data_empty, columns=column_names)
        data_empty = data_empty.fillna("")
        button_select_caout_grid.dataframe(data_empty, height=725)


def set_state_db(session, project_id, app_list):
    set_data("session", session)
    set_data("project_id", project_id)
    set_data("app_list", app_list)
