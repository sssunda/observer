from rest_framework import serializers
from .models import ServerList

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerList
        fields = ['no','server_name', 'server_ip', 'stored_time']