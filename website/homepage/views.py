from django.shortcuts import render
from django.http import HttpResponse
from .models import Sample

def index(request):
    return render(request, 'homepage.html', {'samples': Sample.objects.all})
