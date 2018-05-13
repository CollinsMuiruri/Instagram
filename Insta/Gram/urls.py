from django.conf import settings
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.latest_images,name='latest'),
    url(r'^search/', views.search_results, name='search_results'),
]
