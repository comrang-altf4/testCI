from django.shortcuts import render

from django.http import HttpResponse
from .utils import mySort


def index(request):
    #print value from textbox
    if request.method == "POST":
        return render(request, "homepage.html", {"questions": mySort(request.POST.get("question"))})
    return render(request, "homepage.html", {})
