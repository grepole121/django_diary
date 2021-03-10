from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Entry
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        context = {
            'entries': Entry.objects.filter(author=request.user)
        }
    else:
        context = {"entries": ""}
        messages.info(
                request, f"You haven't submitted an entries yet!")

    return render(request, 'diary/home.html', context)
