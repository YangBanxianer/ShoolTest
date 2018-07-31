#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r"^index/",index_views),
    url(r'^01_request/$',request01_views),
]