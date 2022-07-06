from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def display_topics(request):
    LOT=Topic.objects.all()
    LOW=Webpages.objects.all()
    d={'topics':LOT,'webpages':LOW}
    return render(request,'display_topics.html',d)


