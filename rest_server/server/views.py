from .models import DailyCpu, DailyMem, ServerList
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .serializers import ServerSerializer


@api_view(['GET'])
def view_mem(request, server_name = None):
    if server_name :
        server_list = ServerList.objects.filter(server_name = server_name)
    else :
        server_list = ServerList.objects.all()
    server_list = server_list.values_list('server_name', flat=True)
    data = []

    for server in server_list:
        send_data = {}
        mem_no = DailyMem.objects.filter(server_name = server).order_by('-no').values_list('no',flat=True)[:288]

        mem_query = DailyMem.objects.filter(no__in = list(mem_no)).order_by('no')

        timeseries = list(map(lambda x : x.strftime('%Y-%m-%d %H:%M:%S'), mem_query.values_list('stored_time', flat=True)))
        total_memory = list(mem_query.values_list('total', flat=True))
        available_memory = list(mem_query.values_list('available', flat=True))    
        used_memory = list(mem_query.values_list('used', flat=True))
        free_memory = list(mem_query.values_list('free', flat=True))
        buffers_cached_memory = list(mem_query.values_list('buffers_cached', flat=True))

        send_data['server_name'] = server 
        send_data['data'] = {
            'timeseries' : timeseries,
            'total_memory' : total_memory,
            'available_memory' : available_memory,
            'used_memory' : used_memory,
            'free_memory' : free_memory,
            'buffers_cached_memory' : buffers_cached_memory,
            }

        data.append(send_data)

    if server_name :
        return Response({'data': data[0]['data']})
    return Response({'total': len(server_list), 'data': data})

@api_view(['GET'])
def view_cpu(request, server_name = None):
    if server_name :
        server_list = ServerList.objects.filter(server_name = server_name)
    else :
        server_list = ServerList.objects.all()

    server_list = server_list.values_list('server_name', flat=True)

    data = []

    for server in server_list:
        send_data = {}
        cpu_no = DailyCpu.objects.filter(server_name = server).order_by('-no').values_list('no',flat=True)[:288]

        cpu_query = DailyCpu.objects.filter(no__in = list(cpu_no)).order_by('no')

        timeseries = list(map(lambda x : x.strftime('%Y-%m-%d %H:%M:%S'), cpu_query.values_list('stored_time', flat=True)))
        cpu_core_cnt = list(cpu_query.values_list('core_cnt', flat=True))
        cpu_core_percent = list(cpu_query.values_list('core_percent', flat=True))
        cpu_load_avg_1min = list(cpu_query.values_list('load_avg_1min', flat=True))
        cpu_load_avg_5min = list(cpu_query.values_list('load_avg_5min', flat=True))
        cpu_load_avg_15min = list(cpu_query.values_list('load_avg_15min', flat=True))

        send_data['server_name'] = server 
        send_data['data'] = {
            'timeseries' : timeseries,
            'cpu_core_cnt' : cpu_core_cnt,
            'cpu_core_percent' : cpu_core_percent,
            'cpu_load_avg_1min' : cpu_load_avg_1min,
            'cpu_load_avg_5min' : cpu_load_avg_5min,
            'cpu_load_avg_15min' : cpu_load_avg_15min,
            }

        data.append(send_data)

    if server_name :
        return Response({'data': data[0]['data']})
    return Response({'total': len(server_list), 'data': data})

@api_view(['GET'])
def view_serverlist(request, server_name = None):
    if server_name :
        server_list = ServerList.objects.filter(server_name = server_name)
    else :
        server_list = ServerList.objects.all()

    server_serializer = ServerSerializer(server_list, many = True)
    if server_name :
        return Response({'data':server_serializer.data[0]})
    return Response({'total': len(server_list), 'data':server_serializer.data})
