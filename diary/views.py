from django.shortcuts import render
from .models import Entry
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    if request.user.is_authenticated:
        context = {
            'entries': Entry.objects.filter(author=request.user).order_by("-date_posted")
        }
        if not len(context["entries"]):
            messages.info(request, f"You haven't submitted an entries yet!")

    else:
        context = {"entries": ""}
        messages.info(request, f"You need to login to see your entries!")

    return render(request, 'diary/home.html', context)


# class EntryListView(ListView):
#     model = Entry
#     print(request.user)

#     def get_queryset(self):
#         return self.model.objects.filter(author=self.request.user).order_by("-date_posted")

#     template_name = "diary/home.html"
#     context_object_name = "entries"


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['content']
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
