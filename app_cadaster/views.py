from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html') # Render = criar uma página
