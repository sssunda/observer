from flask import Flask
from flask_socketio import SocketIO
import pymysql

app = Flask(__name__)
soc_io = SocketIO(app)
db = pymysql.connect(host = 'localhost',
                    port = 3306,
                    user = 'observer',
                    passwd = '0326',
                    db = 'observer',
                    charset = 'utf8')
cursor = db.cursor()

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
    VALUES('%s', '%s', sysdate())""" %(server_name, server_ip)

    # execute query
    cursor.execute(sql)

    db.commit()
    
def insert_mem(server_name, server_ip, message):
    sql = """
    INSERT INTO daily_mem(server_name, server_ip, total, available, used, free, buffers_cached, stored_time)
    VALUES('%s', '%s', %d, %d, %d, %d, %d, sysdate())""" %(server_name, server_ip, message['mem_total'], message['mem_available'], message['mem_used'], message['mem_free'], message['mem_buffers_cached'])

    # execute query
    cursor.execute(sql)

    db.commit()

def insert_cpu(server_name, server_ip, message):
    sql = """
    INSERT INTO daily_cpu(server_name, server_ip, core_cnt, core_percent, load_avg_1min, load_avg_5min, load_avg_15min, stored_time)
    VALUES( '%s','%s', %d, %f, %f, %f, %f, sysdate())""" %(server_name, server_ip, message['cpu_core_cnt'], message['cpu_core_percent'], message['cpu_load_avg'][0], message['cpu_load_avg'][1], message['cpu_load_avg'][2])

    # execute query
    cursor.execute(sql)

    db.commit()

if __name__ == '__main__':
    soc_io.run(app)