from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_views(requset):
    return render(requset,'01_xmlhttp.html')
def request01_views(requset):
    return  HttpResponse('这是异步请求的数据')