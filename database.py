import mysql.connector
import pandas as pd
import streamlit as st

def update_outer_exp(conn: mysql.connector.connect, updated_id, teacher_id, location, title):
    cur = conn.cursor()
    
    cur.execute(
        f"""UPDATE 校外經歷
        SET 老師id='{teacher_id}', 校外任職地點='{location}', 校外職稱='{title}'
        WHERE 校外經歷id={updated_id};"""
    )
    conn.commit()

def update_inner_exp(conn: mysql.connector.connect, updated_id, teacher_id, location, title):
    cur = conn.cursor()
    
    cur.execute(
        f"""UPDATE 校內經歷
        SET 老師id='{teacher_id}', 校內任職地點='{location}', 校內職稱='{title}'
        WHERE 校內經歷id={updated_id};"""
    )
    conn.commit()

def update_talent(conn: mysql.connector.connect, updated_id, teacher_id, description):
    cur = conn.cursor()
    
    cur.execute(
        f"""UPDATE 專長
        SET 老師id='{teacher_id}', 專長描述='{description}'
        WHERE 專長id={updated_id};"""
    )
    conn.commit()

def update_background(conn: mysql.connector.connect, updated_id, teacher_id, uni_name, major, degree):
    cur = conn.cursor()
    
    cur.execute(
        f"""UPDATE 學歷
        SET 老師id='{teacher_id}', 大學='{uni_name}', 專業名='{major}', 學碩博='{degree}'
        WHERE 學歷id={updated_id};"""
    )
    conn.commit()
    
def update_course(conn: mysql.connector.connect, updated_id, teacher_id, course_name, class_time, day_in_week):
    cur = conn.cursor()
    
    cur.execute(
        f"""UPDATE 課表
        SET 老師id='{teacher_id}', 課程名稱='{course_name}' , 節次='{class_time}', 星期='{day_in_week}' 
        WHERE 課程id={updated_id};"""
    )
    conn.commit()    
    
def update_journal(conn: mysql.connector.connect, updated_id, teacher_id, name, colaborator, date, category):
    cur = conn.cursor()
    
    cur.execute(
        f"""UPDATE 論文
        SET 老師id='{teacher_id}', 論文名稱='{name}', 共同合作者='{colaborator}', 日期='{date}', 分類='{category}'
        WHERE 論文id={updated_id};"""
    )
    conn.commit()

def delete_outer_exp(conn: mysql.connector.connect, delete_id):
    cur = conn.cursor()
    
    cur.execute(f"DELETE FROM 校外經歷 WHERE 校外經歷id='{delete_id}';")
    conn.commit()
    
def delete_inner_exp(conn: mysql.connector.connect, delete_id):
    cur = conn.cursor()
    
    cur.execute(f"DELETE FROM 校內經歷 WHERE 校內經歷id='{delete_id}';")
    conn.commit()
    
def delete_talent(conn: mysql.connector.connect, delete_id):
    cur = conn.cursor()
    
    cur.execute(f"DELETE FROM 專長 WHERE 專長id='{delete_id}';")
    conn.commit()
    
def delete_background(conn: mysql.connector.connect, delete_id):
    cur = conn.cursor()
    
    cur.execute(f"DELETE FROM 學歷 WHERE 學歷id='{delete_id}';")
    conn.commit()
    
def delete_course(conn: mysql.connector.connect, delete_id):
    cur = conn.cursor()
    
    cur.execute(f"DELETE FROM 課表 WHERE 課程id='{delete_id}';")
    conn.commit()
    
def delete_journal(conn: mysql.connector.connect, delete_id):
    cur = conn.cursor()
    
    cur.execute(f"DELETE FROM 論文 WHERE 論文id='{delete_id}';")
    conn.commit()
    
def read_outer_exp_data(conn: mysql.connector.connect):
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM 校外經歷")
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=['校外經歷id', '老師id', '校外任職地點', '校外職稱'])
      
    return df

def read_inner_exp_data(conn: mysql.connector.connect):
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM 校內經歷")
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=['校內經歷id', '老師id', '校內任職地點', '校內職稱'])
      
    return df

def read_talent_data(conn: mysql.connector.connect):
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM 專長")
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=['專長id', '老師id', '專長描述'])
      
    return df

def read_course_table_data(conn: mysql.connector.connect):
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM 課表")
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=['課程id', '老師id', '課程名稱', '節次', '星期'])
      
    return df

def read_learning_background_data(conn: mysql.connector.connect):
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM 學歷")
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=['學歷id', '老師id', '大學', '專業名', '學碩博'])
      
    return df

def read_journal_data(conn: mysql.connector.connect):
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM 論文")
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=['論文id', '老師id', '論文名稱', '共同合作者', '日期', '分類'])
      
    return df

def create_outer_exp(conn: mysql.connector.connect, outer_exp_id, teacher_id, location, title):
    cur = conn.cursor()
    
    query = f"""
    INSERT INTO 校外經歷
    values ('{outer_exp_id}', '{teacher_id}', '{location}', '{title}');
    """
    cur.execute(query)
    conn.commit()

def create_inner_exp(conn: mysql.connector.connect, inner_exp_id, teacher_id, location, title):
    cur = conn.cursor()
    
    query = f"""
    INSERT INTO 校內經歷
    values ('{inner_exp_id}', '{teacher_id}', '{location}', '{title}');
    """
    cur.execute(query)
    conn.commit()

def create_learning_background(conn: mysql.connector.connect, degree_id, teacher_id, uni_name, major, degree):
    cur = conn.cursor()
    
    query = f"""
    INSERT INTO 學歷
    values ('{degree_id}', '{teacher_id}', '{uni_name}', '{major}', '{degree}');
    """
    cur.execute(query)
    conn.commit()

def create_talent(conn: mysql.connector.connect, talent_id, teacher_id, talent_description):
    cur = conn.cursor()
    query = f"""
    INSERT INTO 專長
    values ('{talent_id}', '{teacher_id}', '{talent_description}');
    """
    cur.execute(query)
    conn.commit()
    
def create_teacher(conn: mysql.connector.connect, teacher_id, teacher_name):
    cur = conn.cursor()
    query = f"""
    INSERT INTO 老師
    values ('{teacher_id}', '{teacher_name}');
    """
    cur.execute(query)
    conn.commit()
    
def create_courses(conn: mysql.connector.connect, course_id, teacher_id, course_name, class_time, day_in_week):
    cur = conn.cursor()
    
    query = f"""
    INSERT INTO 課表
    values ('{course_id}', '{teacher_id}', '{course_name}', '{class_time}', '{day_in_week}');
    """
    cur.execute(query)
    conn.commit()
    
def create_journal(conn: mysql.connector.connect, journal_id, teacher_id, name, collaborator, date, category):
    cur = conn.cursor()
    
    query = f"""
    INSERT INTO 論文
    values ('{journal_id}', '{teacher_id}', '{name}', '{collaborator}', '{date}', '{category}');
    """
    cur.execute(query)
    conn.commit()
    
def create_table_if_not_exist(conn: mysql.connector.connect):
    
    cur = conn.cursor()
    
    
    query = """
    CREATE TABLE IF NOT EXISTS 老師(
        老師id varchar(50),
        名字 varchar(50),
        PRIMARY KEY(老師id)
    );
    """
    cur.execute(query)
    conn.commit()
    query = """
    CREATE TABLE IF NOT EXISTS 論文(
        論文id varchar(50),
        老師id varchar(50),
        論文名稱 varchar(50),
        共同合作者 varchar(50),
        日期 DATE,
        分類 varchar(50),
        PRIMARY KEY(論文id),
        FOREIGN KEY(老師id) REFERENCES 老師(老師id)
    );
    """
    cur.execute(query)
    conn.commit()
    query = """
    CREATE TABLE IF NOT EXISTS 學歷(
        學歷id varchar(50),
        老師id varchar(50),
        大學 varchar(50),
        專業名 varchar(50),
        學碩博 varchar(50),
        PRIMARY KEY(學歷id),
        FOREIGN KEY(老師id) REFERENCES 老師(老師id)
    );
    """
    cur.execute(query)
    conn.commit()
    
    query = """
    CREATE TABLE IF NOT EXISTS 專長(
        專長id varchar(50),
        老師id varchar(50),
        專長描述 varchar(50),
        PRIMARY KEY(專長id),
        FOREIGN KEY(老師id) REFERENCES 老師(老師id)
    );
    """
    cur.execute(query)
    conn.commit()
    
    query = """
    CREATE TABLE IF NOT EXISTS 校內經歷(
        校內經歷id varchar(50),
        老師id varchar(50),
        校內任職地點 varchar(50),
        校內職稱 varchar(50),
        PRIMARY KEY(校內經歷id),
        FOREIGN KEY(老師id) REFERENCES 老師(老師id)
    );
    """
    cur.execute(query)
    conn.commit()
    
    query = """
    CREATE TABLE IF NOT EXISTS 校外經歷(
        校外經歷id varchar(50),
        老師id varchar(50),
        校外任職地點 varchar(50),
        校外職稱 varchar(50),
        PRIMARY KEY(校外經歷id),
        FOREIGN KEY(老師id) REFERENCES 老師(老師id)
    );
    """
        
    cur.execute(query)
    conn.commit()
    
    # 課程id, 老師id, 課程名稱
    query = """
    CREATE TABLE IF NOT EXISTS 課表(
        課程id varchar(50),
        老師id varchar(50),
        課程名稱 varchar(50), 
        節次 INT,
        星期 varchar(10),
        PRIMARY KEY(課程id),
        FOREIGN KEY(老師id) REFERENCES 老師(老師id)
    );
    """
    cur.execute(query)
    conn.commit()

# Connect to database and return the database connection object.
@st.cache_resource
def connect():
    
    
    try:
        # Connect to server
        # MySQL database configuration setup in .streamlit/secrets.toml file.
        connect_db = mysql.connector.connect(**st.secrets["mysql"])
        print("Connect success!")
        
    except Exception as ex:
        print(ex)
        
        
    
    return connect_db
    
    
    
    