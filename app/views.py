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
    LOW=Webpages.objects.order_by(Length('player_name'))[:2:]
    LOA=Access_Records.objects.all()
    d={'topics':LOT,'webpages':LOW,'access':LOA}
    return render(request,'display_topics.html',d)


