import streamlit as st
import shutil
import patoolib
import os
import base64
import secrets
import pandas as pd
from src.db.funtion_database import offline_edit


@st.cache_resource
def get_csrf_token():
    return base64.b64encode(secrets.token_bytes(32)).decode("utf-8")


def update_file_into_server(car_name, List_file, csrf_token):
    if csrf_token != get_csrf_token():
        st.error("Invalid CSRF token. This request is not allowed.")
        return
    if car_name != "":
        car_name = str(car_name).upper()
        folder_save_file_upload = os.path.join('./data', car_name)
        if not os.path.exists(folder_save_file_upload):
            os.makedirs(folder_save_file_upload)
        for file in List_file:
            file_path = os.path.join(folder_save_file_upload, file.name)
            with open(file_path, "wb") as f:
                f.write(file.getvalue())

            # ===================extract file .zip, .7z=======================
            if car_name in file.name and (".zip" in file.name or ".7z" in file.name):
                extract(file_path, folder_save_file_upload)

        if len(List_file) != 0:
            st.write("Update File Completed!!!")


def update_file_after_edit(code, pwt, plant, case, file_updates, csrf_token, name_user):
    flag = 0
    if csrf_token != get_csrf_token():
        # st.error("Invalid CSRF token. This request is not allowed.")
        return "Invalid CSRF token. This request is not allowed."
    for file_update in file_updates:
        if file_update.name == "CADICS_ALL.csv":
            flag = 1
            if code != "" and code != None:
                # try:
                new_data = pd.read_csv(file_update, header=None)
                folder_name = str(name_user).upper() + "_" + str(code).upper() + "_" + str(pwt).upper() + "_" + str(
                    plant).upper() + "_" + str(case).upper()
                folder_save_file_update = os.path.join('./cadic_temp', folder_name, "CADICS_ALL.csv")
                # st.warning(folder_save_file_update)
                if not os.path.exists(folder_save_file_update):
                    return "FAIL: There is no cadic references"
                else:
                    old_data = pd.read_csv(folder_save_file_update, header=None)
                    offline_edit(str(code).upper(), plant, pwt, case, new_data, old_data)
                    return "Update Completed!!!"

            # except:
            #     return "FAIL: ERROR CADICS_ALL.csv!!!"

            else:
                return "Project not exist!!!"
    if flag == 0:
        return "FAIL: Files not CADICS_ALL.csv!!!"


import subprocess


def extract(file_path, output_dir):
    # Tạo thư mục đích nếu nó chưa tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Giải nén tệp .7z vào thư mục đích
    # subprocess.run(["7z","x",file_path,f"-o{output_dir}","-mcp=UTF-8"])
    # patoolib.extract_archive(file_path, outdir=output_dir)
    if ".zip" in file_path:
        subprocess.run(["unar", file_path, "-o", output_dir])
        folder = file_path[0:len(file_path) - 4]
    if ".7z" in file_path:
        subprocess.run(["7z", "x", file_path, f"-o{output_dir}"])
        folder = file_path[0:len(file_path) - 3]
    move_all_items(folder, output_dir)
    delete_folder(folder)


def move_all_items(source_dir, destination_dir):
    # Tạo thư mục đích nếu nó không tồn tại
    os.makedirs(destination_dir, exist_ok=True)

    # Lặp qua tất cả các mục trong thư mục nguồn
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)

        # Di chuyển từng mục sang thư mục đích
        shutil.move(source_item, destination_item)


def delete_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f'Thư mục {folder_path} đã được xóa.')
    else:
        print(f'Thư mục {folder_path} không tồn tại.')
