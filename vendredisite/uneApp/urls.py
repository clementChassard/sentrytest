from django.conf.urls import url

from . import views


app_name = 'uneApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^brokenpage', views.brokenpage, name='brokenpage'),
    url(r'^register', views.register, name='register'),
    url(r'^moncompte/(?P<client_id>[0-9]+)', views.moncompte, name='moncompte'),
]
