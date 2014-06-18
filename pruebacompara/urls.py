from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruebacompara.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/', 'app.views.home', name='home'),

    url(r'^executeprocess/', 'app.views.execute_process', name='execute_process'),
    url(r'^statusprocess/(?P<process_id>\d+)/$', 'app.views.status_process', name='status_process'),

    url(r'^exercise2/$', 'app.views.execute_exercise_2', name='execute_exercise_2'),

    url(r'^admin/', include(admin.site.urls)),

)