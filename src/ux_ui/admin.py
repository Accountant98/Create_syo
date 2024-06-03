import streamlit as st
from streamlit_extras.grid import grid
from .read_data_view import *
from .user_read_only import view
from ..db.function_database_new import querry_data, update_data, update_and_querry_form_data
import re
from ..app.convert_input_to_tuple import dataframe_convert


def reset_data():
    if st.session_state.get('data') is None:
        st.session_state['data'] = {}


def set_data(key: str, value):
    st.session_state['data'][key] = value


def get_data(key):
    return st.session_state['data'].get(key)


def admin():
    reset_data()
    col_left, col_right = st.columns([1, 3])
    with col_left:
        with st.form('仕様表作成_form'):
            # PROJECT BOX
            col_left_prj_grid = grid(1, 1, 2, 2, 1, vertical_align="top")
            # Row 1:
            col_left_prj_grid.header("仕様表作成")
            # Row 2:
            col_left_prj_grid.header("Project Infor")
            # Row 3:
            col_left_prj_grid.text_input("Model Code", key="code")
            col_left_prj_grid.selectbox("PowerTrain", ['EV', 'e-Power', 'ICE'], key="pwt")
            # Row 4:
            col_left_prj_grid.selectbox("Case", ['CASE1', 'CASE1.5', 'CASE2'], key="case")
            col_left_prj_grid.selectbox("Plant", ['JPN', 'US', 'EUR', 'PRC'], key="plant")

            files = st.file_uploader("", accept_multiple_files=False)
            col_left_spec_grid = grid(3, vertical_align="top")
            set_data("running", 0)

            # ==============================================================================================================================

            if col_left_spec_grid.form_submit_button("View", use_container_width=True) and get_data(
                    "running") == 0:
                with st.spinner(text="In progress..."):
                    set_data("running", 1)

                    set_state()
                    if st.session_state.code == '':
                        st.warning("Model code cannot be left blank")
                    else:
                        data, unique_list_max, unique_list_submax = querry_data(st.session_state.code)
                        set_data("仕様表", data)
                        set_data("device_group", unique_list_max)
                        set_data("device", unique_list_submax)

                        set_data("link", "cadics")
                        if not data.empty:
                            print()
                            # st.write("Completed!!!")
                    set_data("running", 0)

            # ==============================================================================================================================

            if col_left_spec_grid.form_submit_button("仕様表Form", use_container_width=True) and get_data(
                    "running") == 0:
                with st.spinner(text="In progress..."):
                    set_data("running", 1)
                    if files is not None:
                        # print("files.name: ", files.name)
                        match = re.search(r'\((.*?)\)', files.name)
                        code = match.group(1).upper()
                        if code != str(st.session_state.code).upper():
                            st.warning("Model code or Spec incorrect")
                        else:
                            df = dataframe_convert(files, str(st.session_state.code).upper())
                            update_data(str(st.session_state.code).upper(), df)
                            set_data("仕様表", data)
                            st.write("Create Completed!!!")
                        set_state()
                    else:
                        st.warning("file has not been uploaded yet")
                    set_data("running", 0)

            if col_left_spec_grid.form_submit_button("仕様表作成",
                                                     use_container_width=True) == True and get_data("running") == 0:
                set_data("running", 1)
                with st.spinner(text="In progress..."):
                    set_state()
                    set_data("running", 0)
        with st.form('仕様表の Format Update'):
            # PROJECT BOX
            col_left_prj_grid = grid(1, vertical_align="top")
            # Row 1:
            col_left_prj_grid.header("仕様表の Format Update")
            files_update = st.file_uploader("", accept_multiple_files=False)
            col_left_spec_grid = grid(2, vertical_align="top")
            set_data("running", 0)

            # ==============================================================================================================================

            if files_update is not None and col_left_spec_grid.form_submit_button("Update",
                                                                                  use_container_width=True) and get_data(
                "running") == 0:
                set_data("running", 1)
                print(files_update.name)
                # df = dataframe_convert(files_update, st.session_state.code)
                # update_data(st.session_state.code, df)
                with st.spinner(text="In progress..."):
                    set_data("running", 0)

            # ==============================================================================================================================

            if col_left_spec_grid.form_submit_button("View database", use_container_width=True) and get_data(
                    "running") == 0:
                with st.spinner(text="In progress..."):
                    set_data("running", 1)
                    set_data("running", 0)
                st.write("Completed!!!")

    with col_right:
        col_r1, col_r2 = st.columns([5, 1])
        with col_r1:
            st.markdown(
                '<h1 style="text-align: center;'
                'background-color: #CCE9D9;'
                'border: 2px solid #4CAF50; '
                'padding: 10px;">仕様表自動作成</h1>',
                unsafe_allow_html=True)
        with col_r2:
            st.markdown(
                f'<p style="text-align: center;'
                f'background-color: #CCE9D9;'
                f'border: 2px solid #4CAF50; '
                f'padding: 10px">{st.session_state.name_user}<br>{st.session_state.position}</p>',
                unsafe_allow_html=True)

        view("admin", st.session_state.code)


def set_state():
    set_data("flag_view", 1)


def set_state_db(session, project_id, app_list):
    set_data("session", session)
    set_data("project_id", project_id)
    set_data("app_list", app_list)
