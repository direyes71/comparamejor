# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from oauthlib import oauth2

import random
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from app.models import Process
from app.tasks import execute_time_process
from app.tasks import get_best_price

# Create your views here.


# Aplication home
def home(request):
    return render_to_response("base.html", locals(), context_instance=RequestContext(request))


# Excercise 1
def execute_process(request):
    # If method is GET
    if request.method == 'GET':
        return render_to_response("execute_process.html", locals(), context_instance=RequestContext(request))
    # Process execution (time=Random)
    process = Process.objects.create(time=random.randint(1, 10))
    execute_time_process.delay(process.id)
    return render_to_response("execute_process.html", locals(), context_instance=RequestContext(request))


# Excercise 2
def execute_exercise_2(request):
    from datetime import datetime
    if request.method == 'POST':
        # Read selected supermarkets
        supermarkets = request.POST.getlist('supermarket')
        if supermarkets:
            print datetime.now()
            less_value = get_best_price(supermarkets)
            print datetime.now()
    return render_to_response("exercise_2.html", locals(), context_instance=RequestContext(request))


def exercise_3(request):
    """
    if request.method == 'POST':
        # Url result with nodejs
        try:
            f = urllib2.urlopen('https://api.instagram.com/oauth/authorize/?client_id=8848927b791649629538c5471281e8f3&response_type=code')
            print f.read()
            f.close()
        except HTTPError, e:
            print u"Ocurrió un error"
            print e.code
        except URLError, e:
            print u"Ocurrió un error"
            print e.reason
    """

    from instagram.client import InstagramAPI
    access_token = "1395575565.8848927.a0b94d2605ac4a24bf89e804b8f16bb2"
    api = InstagramAPI(access_token=access_token)
    print api.user_(user_id=377472509)
    """recent_media, next = api.user_recent_media(user_id=1395575565, count=10)
    for media in recent_media:
       print media.caption.text"""
    return render_to_response("exercise_3.html", locals(), context_instance=RequestContext(request))