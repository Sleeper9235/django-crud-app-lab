from django.shortcuts import render
from .models import Group

# Create your views here.
def home(request):
    groups = Group.objects.all()
    return render(request, 'home.html', {'groups': groups})

def about(request): 
    return render(request, 'about.html')