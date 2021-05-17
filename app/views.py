from django.shortcuts import render

# Create your views here.

def index(request):

    template = 'app/index.html'

    return render(request, template)

def celciusTOfahrenheit(request):

    template = 'app/cf.html'
    
    celcius_value = float(request.GET.get('c_value', False))
    fahrenheit_value = (celcius_value * 9/5) + 32 

    context = {'celcius_value': celcius_value, 'fahrenheit_value': fahrenheit_value}
    return render(request, template, context)
    