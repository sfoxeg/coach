from django.shortcuts import render, redirect
from .models import Services
from .forms import Mastermind_reg_form
from .vk import comments


def index(request):
    services = Services.objects.filter(enable=True)
    return render(
        request,
        "website/index.html",
        context={
            "services": services,
            "comments": comments()
        }
    )


def mm_reg(request):
    if request.method == "POST":
        form = Mastermind_reg_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = Mastermind_reg_form()
    return render(request, 'website/mastermaind_reg.html', {'form': Mastermind_reg_form()})
