

import streamlit as st
import mysql.connector
conn_obj=mysql.connector.connect(
    host=st.secrets["host"],
    database=st.secrets["database"],
    port=st.secrets["port"],
    user=st.secrets["user"],
    password=st.secrets["password"]
)
cursor_obj=conn_obj.cursor(dictionary=True)
#user tables
cursor_obj.execute("""CREATE TABLE IF NOT EXISTS users3(
                   id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(100),
                   email VARCHAR(100) UNIQUE,password VARCHAR(100))""")
########## files table
cursor_obj.execute("""CREATE TABLE IF NOT EXIST files3(
                   id INT PRIMARY KEY AUTO_INCREMENT,user_id INT,file_name VARCHAR(255),
                   file_type VARCHAR(100),file_url TEXT,upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   FOREIGN KEY(user_id) REFERENCES user3(id))""")
conn_obj.commit()
print("Table created successfully")

