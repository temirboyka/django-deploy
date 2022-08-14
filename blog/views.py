from django.shortcuts import render
from .models import Image

def homePage(request):
    images=Image.objects.all()
    context={"images":images}
    return render(request,"home.html",context=context)
