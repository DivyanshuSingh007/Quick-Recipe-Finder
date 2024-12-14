from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"recipe.html")
def paneer(request):
    return render(request,"shahi_paneer.html")
def dal(request):
    return render(request,'dal_makhani.html')
def tea(request):
    return render(request,'tea.html')
def home(request):
    return render(request, 'home.html')


