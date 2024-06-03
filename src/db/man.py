import pandas as pd
import mysql.connector
import numpy as np

# -------------------------- Connect --------------------------------------------------
db_config = {
    'user': 'root',
    'password': 'SQL123456',
    'host': 'localhost',
    'port': 3306,
    'database': 'db_new_prj_final',
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# ------------------------------- Query -------------------------------------------------------
# 1. Select thong tin xe
# sql_query = '''
#             SELECT * FROM information_project W;
#             '''

# 2. Select trang thai thong tin xe
# sql_query = '''
#             SELECT
#                  value_inf.parameter_name,
#                  project.project_name,
#                  config.config_name,
#                  value_inf.value
#             FROM syo_project.value_inf
#             INNER JOIN project ON project.project_id = value_inf.project_id
#             INNER JOIN config ON config.config_id = value_inf.config_id;
#             WHERE project_name = 'WZ1J'
#             '''
# 3. Select thong tin va trang thai cua xe
# sql_query = '''
#             SELECT
#                 value_inf.parameter_name,
#                 information_project.keyword,
#                 information_project.group_infor,
#                 information_project.auto_infor,
#                 project.project_name,
#                 config.config_name,
#                 value_inf.value
#
#             FROM value_inf
#             INNER JOIN project ON project.project_id = value_inf.project_id
#             INNER JOIN config ON config.config_id = value_inf.config_id
#             INNER JOIN information_project ON information_project.parameter_name = value_inf.parameter_name;
#             WHERE project_name = 'WZ1J'
#             '''

# 4. Select toan bo thong tin cua devide+ device detail
# sql_query = '''
#             SELECT
#                 device_details.device_details_name,
#                 device_details.option_detail,
#                 device_details.auto_detail,
#                 device_details.group_detail,
#                 device_details.device_name,
#                 device.device_group
#
#             FROM device_details
#             INNER JOIN device ON device.device_name = device_details.device_name;
#             WHERE project_name = 'WZ1J'
#             '''


# 5. Select toan bo thong tin device detail và trang thai tung config
# sql_query = '''
#             SELECT
#                 project.project_name,
#                 config.config_name,
#                 device_details.device_details_name,
#                 device_details.option_detail,
#                 device_details.auto_detail,
#                 device_details.group_detail,
#                 device_details.device_name,
#                 device.device_group,
#                 status_config_device_detail.status
#
#             FROM status_config_device_detail
#
#             INNER JOIN device_details ON device_details.device_details_id = status_config_device_detail.device_details_id
#             INNER JOIN config ON config.config_id = status_config_device_detail.config_id
#             INNER JOIN project ON project.project_id = status_config_device_detail.project_id
#             INNER JOIN device ON device_details.device_name=device.device_name ;
#             '''

# 6. Select toan bo thong tin comment của tung device detail
sql_query = '''
            SELECT
                project.project_name,
                device_details.device_details_name,
                device_details.group_detail,
                comment_column.comment_name,
                project_device_comment.comment_detail

            FROM project_device_comment
            INNER JOIN device_details ON device_details.device_details_id = project_device_comment.device_details_id
            INNER JOIN project ON project.project_id = project_device_comment.project_id
            INNER JOIN comment_column ON comment_column.comment_id=project_device_comment.comment_id 
            WHERE project_name = 'WZ1J';
            '''


# 7. Select toan bo thong tin lot+option code với từng config
# sql_query = '''
#             SELECT
#                 project.project_name,
#                 config.config_name,
#                 lot.lot_name,
#                 optioncode.optioncode_value,
#                 status_lot_config.status
#
#             FROM status_lot_config
#
#             INNER JOIN project ON project.project_id = status_lot_config.project_id
#             INNER JOIN config ON config.config_id = status_lot_config.config_id
#             INNER JOIN optioncode ON status_lot_config.config_id = optioncode.config_id and status_lot_config.project_id = optioncode.project_id
#             INNER JOIN lot ON lot.lot_id=status_lot_config.lot_id
#             WHERE project_name = 'PZ1L';
#             '''
# 8. Vùng 5'
# sql_query = '''
#             SELECT
#                  project.project_name,
#                  config.config_name,
#                  device_details.device_details_name,
#                  device_details.group_detail,
#                  status_config_device_detail.status
#
#             FROM status_config_device_detail
#             INNER JOIN device_details ON device_details.device_details_id = status_config_device_detail.device_details_id
#             INNER JOIN project ON project.project_id = status_config_device_detail.project_id
#             INNER JOIN config ON config.config_id = status_config_device_detail.config_id
#             WHERE project_name = 'WZ1J';
#             '''
# ------------------------------- Execute -------------------------------------------------------
cursor.execute(sql_query)
result = cursor.fetchall()
print("Kết quả truy vấn:", result)
#
# """
#                 project.project_name,
#                 config.config_name,
#                 device_details.device_details_name,
#                 device_details.option_detail,
#                 device_details.auto_detail,
#                 device_details.group_detail,
#                 device_details.device_name,
#                 device.device_group,
#                 status_config_device_detail.status
# """
# df = pd.DataFrame(result,
#                           columns=['Project', 'Config', 'device_details_name', 'option_detail','auto_detail','group_detail','device_name','device_group', 'status'])
# df.to_excel('trong.xlsx')
