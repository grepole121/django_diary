from django.urls import path
from . import views
from .views import EntryCreateView

urlpatterns = [
    path('', views.home, name="diary-home"),
    path('new/', EntryCreateView.as_view(), name="entry-create"),
]
