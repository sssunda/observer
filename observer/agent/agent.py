import psutil
import socketio
import time

soc_io = socketio.Client()

@soc_io.event
def connect():
    print('connection established')

@soc_io.event
def message():
    mem_info, cpu_info = update_info({}, {})
    soc_io.emit('message' , {'mem_info': mem_info, 'cpu_info':  cpu_info})

@soc_io.event
def disconnect():
    print('disconnected from server')

def update_info(mem_info, cpu_info):
    mem_info = psutil.virtual_memory()
    cpu_info['cpu_core_cnt'] = psutil.cpu_count()
    cpu_info['cpu_core_percent'] = psutil.cpu_percent(interval=0.1, percpu=True)
    cpu_info['cpu_load_avg'] = psutil.getloadavg()

    return mem_info, cpu_info    

# connect to server
soc_io.connect('http://localhost:5000') 

while True :
    time.sleep(3)
    message()