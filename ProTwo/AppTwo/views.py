from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AppTwo.models import Users
from AppTwo.forms import UsersForm

# Create your views here.

def index(request):
    return render(request, "AppTwo/index.html")

def UsersFormView(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR")

    return render(request, 'AppTwo/users.html', {'form': form})