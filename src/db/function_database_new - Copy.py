from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func, and_, MetaData
from hashlib import sha256
from sqlalchemy.orm import sessionmaker, aliased, declarative_base, class_mapper, relationship
import decouple
import pandas as pd
import streamlit as st

# from create_cadics import create_cadics
Base = declarative_base()


class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    comment_name = Column(String, nullable=True)
    config = Column(String, nullable=True)
    project_device_comments = relationship("Project_device_comment", back_populates="comment_ref")


class Config(Base):
    __tablename__ = 'config'

    config_id = Column(Integer, primary_key=True)
    config = Column(String, nullable=True)

    project_has_configs = relationship("Project_has_config", back_populates="config")
    status_lots = relationship("Status_lot", back_populates="config")


class Device(Base):
    __tablename__ = 'device'
    device_name = Column(String, primary_key=True)
    device_group = Column(String, nullable=True)

    # other fields...
    project_has_devices = relationship("Project_has_device", back_populates="device")
    device_details = relationship("Device_details", back_populates="device")


class Device_details(Base):
    __tablename__ = 'device_details'

    device_details_name = Column(String, primary_key=True)
    option_detail = Column(String, nullable=True)
    auto = Column(String, nullable=True)
    group_detail = Column(String, nullable=True)
    device_name = Column(Integer, ForeignKey('device.device_name'))

    # Relationships
    device = relationship("Device", back_populates="device_details")
    project_device_comments = relationship("Project_device_comment", back_populates="device_details")
    status_config_device_details = relationship("Status_config_device_detail", back_populates="device_details")


class Information_project(Base):
    __tablename__ = 'information_project'
    parameter_name = Column(String, primary_key=True)
    keyword = Column(String, nullable=True)
    group_infor = Column(String, nullable=True)
    auto_infor = Column(String, nullable=True)


class Lot(Base):
    __tablename__ = 'lot'
    lot_id = Column(Integer, primary_key=True)
    lot_name = Column(String, nullable=True)


class Project(Base):
    __tablename__ = 'project'

    project_id = Column(Integer, primary_key=True)
    project_name = Column(String, nullable=True)

    project_device_comments = relationship("Project_device_comment", back_populates="project")
    project_has_configs = relationship("Project_has_config", back_populates="project")
    project_has_devices = relationship("Project_has_device", back_populates="project")
    status_config_device_details = relationship("Status_config_device_detail", back_populates="project")
    status_lots = relationship("Project", back_populates="project")


class Project_device_comment(Base):
    __tablename__ = 'project_device_comment'

    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)
    device_details_name = Column(String, ForeignKey('device_details.device_details_name'), primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.comment_id'), primary_key=True)
    comment = Column(String, nullable=True)

    # Relationships
    project = relationship("Project", back_populates="project_device_comments")
    device_details = relationship("Device_details", back_populates="project_device_comments")
    comment_ref = relationship("Comment", back_populates="project_device_comments")


class Project_has_config(Base):
    __tablename__ = 'project_has_config'

    optioncode_value = Column(String, nullable=True)
    config_id = Column(Integer, ForeignKey('config.config_id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)

    # Relationships
    project = relationship("Project", back_populates="project_has_configs")
    config = relationship("Config", back_populates="configs")


class Project_has_device(Base):
    __tablename__ = 'project_has_device'
    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)
    device_name = Column(String, ForeignKey('device.device_name'), primary_key=True)

    # Relationships
    project = relationship("Project", back_populates="project_has_devices")
    device = relationship("Device", back_populates="project_has_devices")


class Status_config_device_detail(Base):
    __tablename__ = 'status_config_device_detail'

    status = Column(String, nullable=True)
    config_id = Column(Integer, ForeignKey('config.config_id'), primary_key=True)
    device_details_name = Column(String, ForeignKey('device_details.device_details_name'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)

    # Relationships
    config = relationship("Config", back_populates="status_config_device_details")
    project = relationship("Project", back_populates="status_config_device_details")
    device_details = relationship("Device_details", back_populates="status_config_device_details")


class Status_lot(Base):
    __tablename__ = 'status_lot'

    status_lot_optioncode = Column(String, nullable=True)
    config_id = Column(Integer, ForeignKey('config.config_id'), primary_key=True)
    lot_id = Column(Integer, ForeignKey('lot.lot_id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)

    # Relationships
    config = relationship("Config", back_populates="status_lots")
    lot = relationship("Lot", back_populates="status_lots")
    project = relationship("Project", back_populates="status_lots")


class Value_inf(Base):
    __tablename__ = 'value_inf'

    value = Column(String, nullable=True)
    project_id = Column(Integer, primary_key=True)
    config_id = Column(Integer, ForeignKey('config.config_id'), primary_key=True)
    parameter_name = Column(Integer, ForeignKey('information_project.parameter_name'), primary_key=True)

    # Relationships
    config = relationship("Config", back_populates="value_infs")
    information_project = relationship("Information_project", back_populates="value_infs")


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    permission = Column(String)
    project = Column(String)


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


def frame_empty():
    data_empty = pd.DataFrame([[""] * 30] * 20)
    column_names = [f'{i + 1}' for i in range(30)]
    data_empty = pd.DataFrame(data_empty, columns=column_names)
    data_empty = data_empty.fillna("")
    return data_empty


def querry_data(project_name):
    engine = connect_db()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    if project_name is not None:
        # project = session.query(Project).filter_by(project_name=project_name).first()
        project = session.query(Project.project_name).all()
        print("project: ", project)
    else:
        session.close()
        st.error("Project not found in the database.")
        return None, frame_empty(), None, None
