from django.conf import settings
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
]
