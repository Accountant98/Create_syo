from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, aliased
import decouple
from hashlib import sha256
from .region1 import *
import numpy as np
from ..app.convert_input_to_tuple import dataframe_convert

Base = declarative_base()


class CommentColumn(Base):
    __tablename__ = 'comment_column'

    comment_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    comment_name = Column(String(45), nullable=False, unique=True)


class Config(Base):
    __tablename__ = 'config'

    config_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    config_name = Column(String(45), nullable=False, unique=True)


class Device(Base):
    __tablename__ = 'device'

    device_name = Column(String(255), primary_key=True, nullable=False)
    device_group = Column(String(255), nullable=True)

    device_details = relationship("DeviceDetails", back_populates="device")
    project_devices = relationship("ProjectDevice", back_populates="device")


class DeviceDetails(Base):
    __tablename__ = 'device_details'

    device_details_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    device_name = Column(String(255), ForeignKey('device.device_name', ondelete='CASCADE', onupdate='CASCADE'),
                         nullable=False)
    device_details_name = Column(String(255), nullable=True)
    group_detail = Column(String(255), nullable=True)
    option_detail = Column(String(500), nullable=True)
    auto_detail = Column(String(255), nullable=True)

    device = relationship("Device", back_populates="device_details")

    __table_args__ = (
        ForeignKeyConstraint(
            ['device_name'],
            ['device.device_name']
        ),
        {'sqlite_autoincrement': True}
    )


class InformationProject(Base):
    __tablename__ = 'information_project'

    parameter_name = Column(String(255), primary_key=True, nullable=False)
    group_infor = Column(String(255), nullable=True)
    keyword = Column(String(255), nullable=True)
    auto_infor = Column(String(255), nullable=True)


class Lot(Base):
    __tablename__ = 'lot'

    lot_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    lot_name = Column(String(45), nullable=False, unique=True)


class OptionCode(Base):
    __tablename__ = 'optioncode'

    config_id = Column(Integer, ForeignKey('config.config_id', ondelete='CASCADE', onupdate='CASCADE'),
                       primary_key=True, nullable=False)
    project_id = Column(Integer, ForeignKey('project.project_id', ondelete='CASCADE', onupdate='CASCADE'),
                        primary_key=True, nullable=False)
    optioncode_value = Column(String(45), nullable=True)


class Project(Base):
    __tablename__ = 'project'

    project_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    project_name = Column(String(45), nullable=False, unique=True)

    project_devices = relationship("ProjectDevice", back_populates="project")


class ProjectDevice(Base):
    __tablename__ = 'project_device'

    device_name = Column(String(255), ForeignKey('device.device_name', ondelete='CASCADE', onupdate='CASCADE'),
                         primary_key=True, nullable=False)
    project_id = Column(Integer, ForeignKey('project.project_id', ondelete='CASCADE', onupdate='CASCADE'),
                        primary_key=True, nullable=False)

    device = relationship("Device", back_populates="project_devices")
    project = relationship("Project", back_populates="project_devices")


class ProjectDeviceComment(Base):
    __tablename__ = 'project_device_comment'

    project_id = Column(Integer, ForeignKey('project.project_id', ondelete='CASCADE', onupdate='CASCADE'),
                        primary_key=True, nullable=False)
    device_details_id = Column(Integer,
                               ForeignKey('device_details.device_details_id', ondelete='CASCADE', onupdate='CASCADE'),
                               primary_key=True, nullable=False)
    comment_id = Column(Integer, ForeignKey('comment_column.comment_id', ondelete='CASCADE', onupdate='CASCADE'),
                        primary_key=True, nullable=False)
    comment_detail = Column(String(500), nullable=True)


class StatusConfigDeviceDetail(Base):
    __tablename__ = 'status_config_device_detail'

    device_details_id = Column(Integer,
                               ForeignKey('device_details.device_details_id', ondelete='CASCADE', onupdate='CASCADE'),
                               primary_key=True, nullable=False)
    config_id = Column(Integer, ForeignKey('config.config_id', ondelete='CASCADE', onupdate='CASCADE'),
                       primary_key=True, nullable=False)
    project_id = Column(Integer, ForeignKey('project.project_id', ondelete='CASCADE', onupdate='CASCADE'),
                        primary_key=True, nullable=False)
    status = Column(String(255), nullable=True)


class StatusLotConfig(Base):
    __tablename__ = 'status_lot_config'

    project_id = Column(Integer, ForeignKey('project.project_id', ondelete='CASCADE', onupdate='CASCADE'),
                        primary_key=True, nullable=False)
    config_id = Column(Integer, ForeignKey('config.config_id', ondelete='CASCADE', onupdate='CASCADE'),
                       primary_key=True, nullable=False)
    lot_id = Column(Integer, ForeignKey('lot.lot_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True,
                    nullable=False)
    status = Column(String(45), nullable=True)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=True)
    permission = Column(String(45), nullable=True)
    project = Column(String(255), nullable=False)


class ValueInf(Base):
    __tablename__ = 'value_inf'

    project_id = Column(Integer, ForeignKey('project.project_id', ondelete='CASCADE', onupdate='CASCADE'),
                        primary_key=True, nullable=False)
    config_id = Column(Integer, ForeignKey('config.config_id', ondelete='CASCADE', onupdate='CASCADE'),
                       primary_key=True, nullable=False)
    parameter_name = Column(String(255),
                            ForeignKey('information_project.parameter_name', ondelete='CASCADE', onupdate='CASCADE'),
                            primary_key=True, nullable=False)
    value = Column(String(45), nullable=True)


def connect_db():
    database_url = decouple.config('DATABASE_URL')
    database_username = decouple.config('DATABASE_USERNAME')
    database_password = decouple.config('DATABASE_PASSWORD')
    database_name = decouple.config('DATABASE_NAME')
    str_connect = "mysql+mysqlconnector://" + database_username + ":" + database_password + "@" + database_url + "/" + database_name
    engine = create_engine(str_connect)
    return engine


def log_in(username, password):
    password = sha256(password.encode('utf-8')).hexdigest()
    # engine = create_engine("mysql+mysqlconnector://test_user_1:Sql123456@10.192.85.133/db_21xe_clone")
    engine = connect_db()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(User.username, User.permission, User.project).filter_by(username=username,
                                                                                   password=password).first()
    if result is not None:
        session.close()
    else:
        session.close()
        result = (username, None, None)
    return result


def replace_symbol(input_text):
    if isinstance(input_text, str):
        for sym in ["<", ">", "\\", "!", "#", "$", "%", "^", "&", "[", "]"]:
            input_text = input_text.replace(sym, "")
        return input_text
    else:
        return input_text


def frame_empty():
    data_empty = pd.DataFrame([[""] * 30] * 20)
    column_names = [f'{i + 1}' for i in range(30)]
    data_empty = pd.DataFrame(data_empty, columns=column_names)
    data_empty = data_empty.fillna("")
    return data_empty


def querry_data(project_name):
    project_name = project_name.upper()
    engine = connect_db()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_project = [name[0] for name in session.query(Project.project_name).all()]
    if project_name in all_project:
        result_querry_region1 = session.query(InformationProject).all()
        df_1 = region_1(result_querry_region1)

        # ORM Query
        querry_2 = session.query(ValueInf.parameter_name, Project.project_name, Config.config_name, ValueInf.value) \
            .join(Project, Project.project_id == ValueInf.project_id) \
            .join(Config, Config.config_id == ValueInf.config_id) \
            .filter(Project.project_name == project_name)
        result_querry_region2 = querry_2.all()
        df_2 = region_2(result_querry_region2)
        merged_df_1_2 = pd.merge(df_1, df_2, on='CADICS ID', how='inner')
        #
        result_querry_region3 = session.query(ValueInf.parameter_name, InformationProject.keyword,
                                              InformationProject.group_infor, InformationProject.auto_infor,
                                              Project.project_name, Config.config_name, ValueInf.value) \
            .join(Project, Project.project_id == ValueInf.project_id) \
            .join(Config, Config.config_id == ValueInf.config_id) \
            .join(InformationProject, InformationProject.parameter_name == ValueInf.parameter_name) \
            .filter(Project.project_name == project_name) \
            .all()
        # print("result_querry_region3:", result_querry_region3)
        df_3 = region_3(result_querry_region3)

        # Truy vấn với ORM
        results_querry_region_4 = session.query(DeviceDetails.device_details_name, DeviceDetails.option_detail,
                                                DeviceDetails.auto_detail,
                                                DeviceDetails.group_detail, DeviceDetails.device_name,
                                                Device.device_group) \
            .join(Device, Device.device_name == DeviceDetails.device_name) \
            .filter(Project.project_name == project_name) \
            .all()
        index_df_1 = df_1.index.max()
        # print("results_querry_region_4: ", results_querry_region_4)
        df_4, unique_list_max, unique_list_submax = region_4(results_querry_region_4, index_df_1)

        results_querry_region_7 = session.query(
            Project.project_name,
            Config.config_name,
            Lot.lot_name,
            OptionCode.optioncode_value,
            StatusLotConfig.status
        ).join(
            StatusLotConfig, Project.project_id == StatusLotConfig.project_id
        ).join(
            Config, Config.config_id == StatusLotConfig.config_id
        ).join(
            OptionCode,
            (OptionCode.config_id == StatusLotConfig.config_id) & (OptionCode.project_id == StatusLotConfig.project_id)
        ).join(
            Lot, Lot.lot_id == StatusLotConfig.lot_id
        ).filter(
            Project.project_name == project_name
        ).all()
        index_df_4 = df_4.index.max()
        # print("results_querry_region_7: ", results_querry_region_7)
        df_7 = region_7(results_querry_region_7, index_df_4)
        # merged_df_4_7 = pd.concat([merged_df_1_2, df_4, df_7], axis=0)

        # Truy vấn ORM
        querry_region_8 = session.query(
            Project.project_name,
            Config.config_name,
            DeviceDetails.device_details_name,
            DeviceDetails.group_detail,
            StatusConfigDeviceDetail.status
        ).join(
            DeviceDetails, StatusConfigDeviceDetail.device_details_id == DeviceDetails.device_details_id
        ).join(
            Project, StatusConfigDeviceDetail.project_id == Project.project_id
        ).join(
            Config, StatusConfigDeviceDetail.config_id == Config.config_id
        ).filter(
            Project.project_name == project_name
        )

        results_querry_region_8 = querry_region_8.all()
        # print(results_querry_region_8)
        df_8 = region_8(results_querry_region_8)
        merged_df_4_8 = pd.merge(df_4, df_8, on=['gr', 'CADICS ID'], how='left')
        merged_df_4_8.set_index(df_4.index, inplace=True)
        merged_df_1_2_4_7_8 = pd.concat([merged_df_1_2, merged_df_4_8, df_7], axis=0)

        results_querry_region_6 = session.query(
            Project.project_name,
            DeviceDetails.device_details_name,
            DeviceDetails.group_detail,
            CommentColumn.comment_name,
            ProjectDeviceComment.comment_detail
        ).join(ProjectDeviceComment, Project.project_id == ProjectDeviceComment.project_id
               ).join(DeviceDetails, DeviceDetails.device_details_id == ProjectDeviceComment.device_details_id
                      ).join(CommentColumn, CommentColumn.comment_id == ProjectDeviceComment.comment_id
                             ).filter(Project.project_name == project_name).all()
        df_6 = region_6(results_querry_region_6)
        merged_df_1_2_4_6_7_8 = pd.merge(merged_df_1_2_4_7_8, df_6, on=['gr', 'CADICS ID'], how='left')
        # merged_df_1_2_4_6_8.set_index(merged_df_1_2_4_8.index, inplace=True)
        session.close()
        return merged_df_1_2_4_6_7_8, unique_list_max, unique_list_submax
    else:
        session.close()
        st.error("Project not found in the database.")
        return frame_empty(), [], []


# def update_and_querry_form_data(project_name):
#     project_name = project_name.upper()
#     engine = connect_db()
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     all_project = [name[0] for name in session.query(Project.project_name).all()]
#     if project_name in all_project:
#         result_querry_region1 = session.query(InformationProject).all()
#         df_1 = region_1(result_querry_region1)
#
#         # ORM Query
#         querry_2 = session.query(ValueInf.parameter_name, Project.project_name, Config.config_name, ValueInf.value) \
#             .join(Project, Project.project_id == ValueInf.project_id) \
#             .join(Config, Config.config_id == ValueInf.config_id) \
#             .filter(Project.project_name == project_name)
#         result_querry_region2 = querry_2.all()
#         df_2 = region_2(result_querry_region2)
#         merged_df_1_2 = pd.merge(df_1, df_2, on='CADICS ID', how='inner')
#
#         results_querry_region_4 = session.query(DeviceDetails.device_details_name, DeviceDetails.option_detail,
#                                                 DeviceDetails.auto_detail,
#                                                 DeviceDetails.group_detail, DeviceDetails.device_name,
#                                                 Device.device_group) \
#             .join(Device, Device.device_name == DeviceDetails.device_name) \
#             .filter(Project.project_name == project_name) \
#             .all()
#         index_df_1 = df_1.index.max()
#         df_4, unique_list_max, unique_list_submax = region_4(results_querry_region_4, index_df_1)
#
#         results_querry_region_7 = session.query(
#             Project.project_name,
#             Config.config_name,
#             Lot.lot_name,
#             OptionCode.optioncode_value,
#             StatusLotConfig.status
#         ).join(
#             StatusLotConfig, Project.project_id == StatusLotConfig.project_id
#         ).join(
#             Config, Config.config_id == StatusLotConfig.config_id
#         ).join(
#             OptionCode,
#             (OptionCode.config_id == StatusLotConfig.config_id) & (OptionCode.project_id == StatusLotConfig.project_id)
#         ).join(
#             Lot, Lot.lot_id == StatusLotConfig.lot_id
#         ).filter(
#             Project.project_name == project_name
#         ).all()
#         index_df_4 = df_4.index.max()
#         df_7 = region_7(results_querry_region_7, index_df_4)
#         merged_df_4_7 = pd.concat([merged_df_1_2, df_4, df_7], axis=0)
#         session.close()
#         return merged_df_4_7, unique_list_max, unique_list_submax
#     else:
#         session.close()
#         st.error("Project not found in the database.")
#         return frame_empty(), [], []


def update_and_querry_form_data(project_name, file_name):
    project_name = project_name.upper()
    engine = connect_db()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_project = [name[0] for name in session.query(Project.project_name).all()]



def update_data(project_name, df):
    project_name = str(project_name).upper()
    engine = connect_db()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    df.replace({np.nan: ''}, inplace=True)
    existing_project = (session.query(Project).filter_by(project_name=project_name).first())
    if existing_project is not None:
        project_id = existing_project.id_project
    else:
        project = Project(project_name=project_name)
        session.add(project)
        session.commit()
    return session, df
