from django.shortcuts import render
from .models import movie
from .models import actor

# Create your views here.
def index(request):
    mov = movie.objects.all()
    act = actor.objects.all()
    return render(request,"index.html",{'movies':mov,'actors':act})
