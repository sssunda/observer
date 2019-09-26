from django.db import models

class DailyCpu(models.Model):
    no = models.AutoField(primary_key=True)
    server_name = models.CharField(max_length=30, blank=True, null=True)
    server_ip = models.CharField(max_length=15, blank=True, null=True)
    core_cnt = models.IntegerField(blank=True, null=True)
    core_percent = models.FloatField(blank=True, null=True)
    load_avg_1min = models.FloatField(blank=True, null=True)
    load_avg_5min = models.FloatField(blank=True, null=True)
    load_avg_15min = models.FloatField(blank=True, null=True)
    stored_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'daily_cpu'


class DailyMem(models.Model):
    no = models.AutoField(primary_key=True)
    server_name = models.CharField(max_length=30, blank=True, null=True)
    server_ip = models.CharField(max_length=15, blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    available = models.BigIntegerField(blank=True, null=True)
    used = models.BigIntegerField(blank=True, null=True)
    free = models.BigIntegerField(blank=True, null=True)
    buffers_cached = models.BigIntegerField(blank=True, null=True)
    stored_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'daily_mem'

class ServerList(models.Model):
    no = models.AutoField(primary_key=True)
    server_name = models.CharField(max_length=30, blank=True, null=True)
    server_ip = models.CharField(max_length=15, blank=True, null=True)
    stored_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'server_list'
