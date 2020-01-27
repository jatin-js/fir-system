from django.shortcuts import render
from .models import Crime

def crime(request):
    crime = Crime.objects.all()
    return render(request, 'crime.html', {'crime': crime})
# Create your views here.
