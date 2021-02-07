import configparser
import configparser

import mysql.connector
from mysql.connector import Error

def getconfig():
    config = configparser.ConfigParser()
    config.read('C:/Users/Lenovo/Desktop/PythonPractice/Final_Automation_Practice/API/utilities/properties.ini')
    return config

connect_config={
    'user':getconfig()['SQL']['user'],
    'host':getconfig()['SQL']['host'],
    'database':getconfig()['SQL']['database'],
    'password':getconfig()['SQL']['password']
}

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("COnnection succesful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
