from django.shortcuts import render
from django.http import HttpResponse
from django.db.


# Create your views here.
def login_views(request):
    return HttpResponse("i am first django proces")

def authors_views(request):
    return render(request,03_authors.html)

def doF_views(request):
    Author.objects.all().update(age=F('age ')+10)
    return  HttpResponse("updata Age ok")