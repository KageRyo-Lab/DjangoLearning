from django.shortcuts import render

def index(request):
    context = {}
    context['name'] = "KageRyo"
    return render(request, 'index.html', context)

def index1(request):
    context = {}
    context['name'] = "KageRyo"
    return render(request, 'index1.html', context)