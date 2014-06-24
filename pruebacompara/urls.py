# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruebacompara.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', 'app.views.home', name='home'),
    url(r'^home/', 'app.views.home', name='home'),

    url(r'^executeprocess/', 'app.views.execute_process', name='execute_process'),

    url(r'^exercise2/$', 'app.views.execute_exercise_2', name='execute_exercise_2'),

    url(r'^exercise3/$', 'app.views.exercise_3', name='exercise_3'),

    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),

    url(r'^admin/', include(admin.site.urls)),

)