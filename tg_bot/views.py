from django.shortcuts import render
from website.models import Services


# Create your views here.
def cat(request):
    services = Services.objects.filter(enable=True)
    return render(
        request,
        "tg_bot/cat.html",
        context={
            "services": services
        }
    )
