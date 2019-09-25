import psutil
import socketio
import time
import socket

soc_io = socketio.Client()
server_name = socket.gethostname()
server_ip = socket.gethostbyname(server_name)

@soc_io.event
def connect():    
    print('connection established')

@soc_io.event
def message():
    mem_info, cpu_info = update_info({}, {})    
    soc_io.emit('message' , {'server_name' : server_name, 'server_ip':server_ip, 'mem_info': mem_info, 'cpu_info':  cpu_info})

@soc_io.event
def disconnect():
    print('disconnected from server')

def update_info(mem_info, cpu_info):
    mem_info_all = psutil.virtual_memory()
    mem_info['mem_total'] = mem_info_all[0]
    mem_info['mem_available'] = mem_info_all[1]
    mem_info['mem_used'] = mem_info_all[3]
    mem_info['mem_free'] = mem_info_all[4]
    mem_info['mem_buffers_cached'] = mem_info_all[7] + mem_info_all[8]

    cpu_info['cpu_core_cnt'] = psutil.cpu_count()
    cpu_info['cpu_core_percent'] = psutil.cpu_percent(interval=0.1, percpu=True)
    cpu_info['cpu_load_avg'] = psutil.getloadavg()

    return mem_info, cpu_info    

# connect to server
soc_io.connect('http://localhost:5000') 

while True :
    time.sleep(3)
    message()