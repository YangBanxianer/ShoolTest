from django.conf.urls import url
from .views import *

urlpatterns= [
    url(r'^login/$',login_views),
    url(r'^03_authors/',authors_views),
]