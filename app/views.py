from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length

# Create your views here.
from app.models import *

def display_topics(request):
    LOT=Topic.objects.all()
    # LOW=Webpages.objects.filter(player_name='YASH')
    # LOW=Webpages.objects.order_by('player_name')
    # LOW=Webpages.objects.order_by('-player_name')
    # LOW=Webpages.objects.order_by(Length('player_name').desc())
    # LOW=Webpages.objects.exclude(player_name='YASH')
    # LOW=Webpages.objects.order_by(Length('player_name'))[:2:]
    
    LOW=Webpages.objects.all()
    LOA=Access_Records.objects.all()
    d={'topics':LOT,'webpages':LOW,'access':LOA}
    return render(request,'display_topics.html',d)

def update_web(request):
    Webpages.objects.filter(topic_name='CRICKET').update(player_name='HARITHA')
    t=Topic.objects.get_or_create(topic_name='RUBBY')[0]
    t.save()
    Webpages.objects.update_or_create(topic_name='RUBBY',defaults={'topic_name':t,'player_name':'kamal','url':'https://kamal.com'})
    LOW=Webpages.objects.all()
    d={'ws':Webpages}
    return render(request,'display_topics.html',d)

def delete_web(request):
    Webpages.objects.filter(player_name='kamal').delete()
    # Webpages.objects.all().delete()
    Webapges=Webpages.objects.all()
    d={'ws':Webpages}
    return render(request,'display_topics.html',d)

