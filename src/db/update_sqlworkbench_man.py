import pandas as pd
import mysql.connector
import numpy as np
# Thay đổi các thông số kết nối dựa trên cấu hình của bạn
db_config = {
    'user': 'root',
    'password': 'SQL12345',
    'host': 'localhost',
    'port': 3306,
    'database': 'syo_project',
}

# Tạo kết nối MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()
print("ok")

# Đường dẫn đến tệp CSV
csv_file_path = r"C:\Users\KNT21675\Desktop\table\valua_inf.xlsx"

# Đọc tệp CSV vào DataFrame, bắt đầu từ dòng tiêu đề cột
df = pd.read_excel(csv_file_path)
df.fillna('null', inplace=True)
print(df)
errors = []
print("ok hi")

for index, row in df.iterrows():

    try:
        # query = f"""INSERT INTO device_details (device_details_id,device_name,device_details_name,group_detail, option_detail, auto_detail) VALUES (%s, %s, %s, %s, %s, %s)"""
        # val = (row['device_details_id'],row['device_name'], row['device_details_name'], row['group_detail'], row['option_detail'], row['auto_detail'])  # Thay 'column1', 'column2', 'column3' với tên cột của bạn
        
        # query = f"""INSERT INTO project_device_comment (project_id, device_details_id, comment_id, comment_detail) VALUES (%s, %s, %s, %s)"""
        # val = (row['project_id'], row['device_details_id'], row['comment_id'], row['comment_detail'])
        
        # query = f"""INSERT INTO status_config_device_detail (device_details_id, config_id, project_id, status) VALUES (%s, %s, %s, %s)"""
        # val = (row['device_details_id'], row['config_id'], row['project_id'], row['status'])

        query = f"""INSERT INTO value_inf (project_id, config_id, parameter_name, value) VALUES (%s, %s, %s, %s)"""
        val = (row['project_id'], row['config_id'], row['parameter_name'], row['value'])
        
        # query = f"""INSERT INTO device (device_name, device_group) VALUES (%s, %s)"""
        # val = (row['device_name'], row['device_group'])

        # query = f"""INSERT INTO information_project (parameter_name, group_infor , keyword,auto_infor) VALUES (%s, %s,%s, %s)"""
        # val = (row['parameter_name'], row['keyword'],row['group_infor'], row['auto_infor'])

        # query = f"""INSERT INTO optioncode (config_id, project_id , optioncode_value) VALUES (%s, %s,%s)"""
        # val = (row['config_id'], row['project_id'],row['optioncode_value'])

        # query = f"""INSERT INTO project_device (device_name, project_id) VALUES (%s, %s)"""
        # val = (row['device_name'], row['project_id'])

        # query = f"""INSERT INTO status_lot_config (project_id, config_id,lot_id,status) VALUES (%s, %s,%s, %s)"""
        # val = (row['project_id'], row['config_id'],row['lot_id'], row['status_lot'])
        print(val)
        cursor.execute(query, val)# Lưu thay đổi vào cơ sở dữ liệu
        conn.commit()


    except mysql.connector.IntegrityError as e:
        # print("IntegrityError: ", e)
        errors.append(row['device_details_name'])

conn.close()
print(errors)
