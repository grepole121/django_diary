from django.shortcuts import render
from .models import Entry


def home(request):
    context = {
        'entries': Entry.objects.all()
    }
    return render(request, 'diary/home.html', context)
