import random
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.template.context import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from app.models import Process

# Create your views here.
from celery import group
from app.tasks import execute_time_process
from app.tasks import ask_super_market

from app.tasks import *


def home(request):
    return render_to_response("base.html", locals(), context_instance=RequestContext(request))


def execute_process(request):
    if request.method == 'GET':
        return render_to_response("execute_process.html", locals(), context_instance=RequestContext(request))
    process = Process.objects.create(time=random.randint(1, 10))
    execute_time_process.delay(process.id)
    return render_to_response("execute_process.html", locals(), context_instance=RequestContext(request))


@csrf_exempt
def status_process(request, process_id):
    process = Process.objects.get(id=process_id)
    if process.status == 2:
        return HttpResponse(simplejson.dumps({'successful': 1, 'message': 'El proceso ha finalizado'}))
    return HttpResponse(simplejson.dumps({'successful': 2, 'remaining_time': process.remaining_time(), 'message': 'El proceso no ha finalizado'}))


def execute_exercise_2(request):
    if request.method == 'POST':
        from datetime import datetime
        supermarkets = request.POST.getlist('supermarket')
        if supermarkets:
            print datetime.now()
            result = group(ask_super_market.s(int(supermarket)) for supermarket in supermarkets).apply_async()
            values = result.get()
            less_value = None
            for supermarket, value in values:
                if less_value == None:
                    less_value = {'supermarket': supermarket, 'value': value}
                elif value < less_value['value']:
                    less_value = {'supermarket': supermarket, 'value': value}
            print less_value['value']
            print datetime.now()
    return render_to_response("exercise_2.html", locals(), context_instance=RequestContext(request))