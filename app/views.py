from django.shortcuts import render, HttpResponse
from .forms import length_conversion, weight_conversion, temperature_conversion

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')

conversion_factors_length = {
    "mm": 1,
    "cm": 10,
    "m": 1000,
    "km": 1000000,
    "in": 25.4,
    "ft": 304.8,
    "yd": 914.4,
    "mi": 1609344,
}

conversion_factors_weight = {
    "mg": 1, 
    "g": 1000,
    "kg": 1000000,
    "oz": 28349.5, 
    "lb": 453592.37,
}


def length(request):
    result = None

    if request.method == 'POST':
        form = length_conversion(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            result = round(value * conversion_factors_length[from_unit] / conversion_factors_length[to_unit], 2)
    else:
        form = length_conversion()

    return render(request, 'length.html', {'form':form, 'result':result})

def weight(request):
    result = None

    if request.method == 'POST':
        form = weight_conversion(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            result = round(value * conversion_factors_weight[from_unit] / conversion_factors_weight[to_unit], 2)
    else:
        form = weight_conversion()

    return render(request, 'weight.html', {'form':form, 'result':result})

def temperature(request):
    result = None

    if request.method == 'POST':
        form = temperature_conversion(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            celsius_value = to_celsius(value, from_unit)
            result = round(from_celsius(celsius_value, to_unit), 2)
    else:
        form = temperature_conversion()

    return render(request, 'weight.html', {'form':form, 'result':result})

def to_celsius(value, from_unit):
    """Convert any unit to Celsius first."""
    if from_unit == "C":
        return value
    elif from_unit == "F":
        return (value - 32) * 5/9
    elif from_unit == "K":
        return value - 273.15
    else:
        raise ValueError("Unsupported unit")

def from_celsius(value, to_unit):
    """Convert Celsius to the target unit."""
    if to_unit == "C":
        return value
    elif to_unit == "F":
        return (value * 9/5) + 32
    elif to_unit == "K":
        return value + 273.15
    else:
        raise ValueError("Unsupported unit")

