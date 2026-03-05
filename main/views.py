from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request, "home.html")


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, "contact.html")