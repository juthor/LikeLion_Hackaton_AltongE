from django.shortcuts import render

# Create your views here.
def daily(request):
    return render(request, 'daily.html')