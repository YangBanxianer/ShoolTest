from django.conf.urls import url
from .views import *
from django.conf.urls import url,include

urlpatterns= [
    url(r'^',include('index.urls')),
    url(r'^login/$',login_views),
]