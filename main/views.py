from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .forms import NameForm


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponse('/thanks/')
    else:
        form = NameForm()

    return render(request, 'name.html', {'form' : form})


def login_view_test(request):
    return render(request, 'mylogin.html')