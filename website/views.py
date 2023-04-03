from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Services
from .forms import mastermaind_reg_form
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
    # Если что-то пришло
    if request.method == "POST":
        form = mastermaind_reg_form(request.POST)
        fio = form.cleaned_data['fio']
        phoneNumber = form.cleaned_data['phoneNumber']
        email = form.cleaned_data['email']
        request = form.cleaned_data['request']
        # То проверяем валидны ли данные
        if form.is_valid():
            print(fio)
            return HttpResponseRedirect("/")
        else:
            # Если не валидны, просто перезагрузим форму
            form = mastermaind_reg_form(initial={
                'fio': fio,
                'phoneNumber': phoneNumber,
                'email': email,
                'request': request
            })
            return render(request, "website/mastermaind_reg.html", {'form': form})
    else:
        return render(request, "website/mastermaind_reg.html", {'form': mastermaind_reg_form()})

