from django.shortcuts import render, HttpResponse
from .forms import length_conversion

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')

conversion_factors = [
    'm':1,
    'km':1000,
    'cm':0.01,
    'mm':0.001,
    'mi': 1609.34,
    'yd': 0.9144,
    'ft': 0.3048,
    'in': 0.0254,
]

def length(request):
    result = None

    if request.method == 'POST':
        form = length_conversion(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            in_meters = value * conversion_factors[from_unit]
            result = in_meters * conversion_factors[to_unit]
    else:
        form = length_conversion()

    return render(request, 'length.html', {'form':form, 'result':result})
