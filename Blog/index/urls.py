#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns= [
    url(r'^',include('index.urls')),
    url(r'^index/$',index_views),
]