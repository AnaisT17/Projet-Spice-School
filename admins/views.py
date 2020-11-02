from django.shortcuts import render
import admins

def home(request):
    return render(request, "templates/admins/index.html", {})