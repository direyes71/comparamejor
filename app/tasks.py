from celery import task
import time
from app.models import Process


@task
def execute_time_process(process_id):
    for tmp in range(1, Process.objects.get(id=process_id).time+1):
        time.sleep(1)
        Process.objects.filter(id=process_id).update(time_executed=tmp)

    Process.objects.filter(id=process_id).update(status=2)


VALUES_SUPER_MARKETS = {'exito': 1000, 'carulla': 1500, 'otro': 2000}

@task
def ask_super_market(supermarket):
    for tmp in range(1, 5):
        time.sleep(1)
    return VALUES_SUPER_MARKETS[supermarket]