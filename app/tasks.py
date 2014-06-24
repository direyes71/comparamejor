# -*- coding: utf-8 -*-


from celery import task
from celery import chord
import time
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from app.models import Process


# Execute a process with a specific time
@task
def execute_time_process(process_id):
    for tmp in range(1, Process.objects.get(id=process_id).time+1):
        time.sleep(1)
        Process.objects.filter(id=process_id).update(time_executed=tmp)

    # Upgrade process status
    Process.objects.filter(id=process_id).update(status=2)

    # Url result with nodejs
    try:
        f = urllib2.urlopen('http://localhost:8086/resultclient/' + str(process_id) + '/')
        print f.read()
        f.close()
    except HTTPError, e:  
        print u"Ocurrió un error"
        print e.code  
    except URLError, e:
        print u"Ocurrió un error"
        print e.reason


# Constants supermarkets
EXITO = 1
CARULLA = 2
OXXO = 3
SAO = 4
JUMBO = 5

# Prices for each supermarket
VALUES_SUPER_MARKETS = {EXITO: 1000, CARULLA: 1500, OXXO: 200, SAO: 2500, JUMBO: 3000}

# Labels supermarkets
SUPERMARKETS = ["EXITO", "CARULLA", "OXXO", "SAO", "JUMBO"]

# Task for question in a specific supermarket
@task
def ask_super_market(supermarket):
    supermarket = int(supermarket)
    time.sleep(5)
    return (SUPERMARKETS[supermarket-1], VALUES_SUPER_MARKETS[supermarket])

# Task for calculate less value between a supermarkets list
@task
def calculate_best_price(values_supermarkets):
    less_value = None
    for supermarket, value in values_supermarkets:
        if less_value == None:
            less_value = {'supermarket': supermarket, 'value': value}
        elif value < less_value['value']:
            less_value = {'supermarket': supermarket, 'value': value}
    return less_value

# Return the supermarket with less value
def get_best_price(supermarkets):
    callback = calculate_best_price.subtask()
    header = [ask_super_market.subtask(args=(supermarket)) for supermarket in supermarkets]
    result = chord(header, callback, interval=1).delay()
    return result.get()