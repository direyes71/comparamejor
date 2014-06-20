from celery import task
import time
from app.models import Process


@task
def execute_time_process(process_id):
    for tmp in range(1, Process.objects.get(id=process_id).time+1):
        time.sleep(1)
        Process.objects.filter(id=process_id).update(time_executed=tmp)

    Process.objects.filter(id=process_id).update(status=2)


EXITO = 1
CARULLA = 2
OXXO = 3
SAO = 4
JUMBO = 5

VALUES_SUPER_MARKETS = {EXITO: 1000, CARULLA: 1500, OXXO: 200, SAO: 2500, JUMBO: 3000}

SUPERMARKETS = ["EXITO", "CARULLA", "OXXO", "SAO", "JUMBO"]

@task
def ask_super_market(supermarket):
    time.sleep(5)
    return (SUPERMARKETS[supermarket-1], VALUES_SUPER_MARKETS[supermarket])