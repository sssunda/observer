from flask import Flask
from flask_socketio import SocketIO
import sqlite3

app = Flask(__name__)
soc_io = SocketIO(app)
db = sqlite3.connect('../../observer.db', check_same_thread=False)
cursor = db.cursor()

# create tble
query = """
CREATE TABLE IF NOT EXISTS server_list(
    no INTEGER PRIMARY_KEY autoincrement,
    server_name TEXT, 
    server_ip TEXT,
    stored_time DATETIME)
"""
cursor.execute(query)

query = """
CREATE TABLE IF NOT EXISTS daily_mem(
    no INTEGER PRIMARY KEY autoincrement,
    server_name TEXT,
    server_ip TEXT,
    total INTEGER,
    available INTEGER,
    used INTEGER,
    free INTEGER,
    buffers_cached INTEGER,
    stored_time DATETIME);
"""
cursor.execute(query)

query = """
CREATE TABLE IF NOT EXISTS daily_cpu(
    no INTEGER PRIMARY KEY autoincrement,
    server_name TEXT,
    server_ip TEXT,
    core_cnt INTEGER,
    core_percent INTEGER,
    load_avg_1min INTEGER,
    load_avg_5min INTEGER,
    load_avg_15min INTEGER,
    stored_time DATETIME);
"""
cursor.execute(query)

@app.route('/')
def index():
    return "This is observer's server"

@soc_io.on("connect")
def connect():
    print('success to connect')

@soc_io.on("message")
def handle_message(message):
    server_name = message['server_name']
    server_ip = message['server_ip']

    # It's first time
    if not check_server(server_name, server_ip) :
        insert_server(server_name, server_ip)

    insert_mem(server_name, server_ip, message['mem_info'])
    insert_cpu(server_name, server_ip, message['cpu_info'])

def check_server(server_name, server_ip):
    sql = """
    SELECT * 
    FROM server_list
    WHERE server_name = '""" + server_name + "' and server_ip = '" + server_ip +"'"
    cursor.execute(sql)
    result = cursor.fetchall()

    return result

def insert_server(server_name, server_ip):
    sql = """
    INSERT INTO server_list(server_name, server_ip, stored_time)
    VALUES('%s', '%s', datetime())""" %(server_name, server_ip)

    # execute query
    cursor.execute(sql)

    db.commit()
    
def insert_mem(server_name, server_ip, message):
    sql = """
    INSERT INTO daily_mem(server_name, server_ip, total, available, used, free, buffers_cached, stored_time)
    VALUES('%s', '%s', %d, %d, %d, %d, %d, datetime())""" %(server_name, server_ip, message['mem_total'], message['mem_available'], message['mem_used'], message['mem_free'], message['mem_buffers_cached'])

    # execute query
    cursor.execute(sql)

    db.commit()

def insert_cpu(server_name, server_ip, message):
    sql = """
    INSERT INTO daily_cpu(server_name, server_ip, core_cnt, core_percent, load_avg_1min, load_avg_5min, load_avg_15min, stored_time)
    VALUES( '%s','%s', %d, %f, %f, %f, %f, datetime())""" %(server_name, server_ip, message['cpu_core_cnt'], message['cpu_core_percent'], message['cpu_load_avg'][0], message['cpu_load_avg'][1], message['cpu_load_avg'][2])

    # execute query
    cursor.execute(sql)

    db.commit()

if __name__ == '__main__':
    soc_io.run(app, host = "0.0.0.0")