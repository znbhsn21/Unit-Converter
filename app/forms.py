from django import forms

class length_conversion(forms.Form):
    length_units = [
        ('m', 'Meters'),
        ('km', 'Kilometers'),
        ('cm', 'Centimeters'),
        ('mm', 'Millimeters'),
        ('mi', 'Miles'),
        ('yd', 'Yards'),
        ('ft', 'Feet'),
        ('in', 'Inches'),
    ]

    value = forms.FloatField(label = 'Enter Value',
                            widget = forms.NumberInput(attrs = {
                                'class':'form-control',
                                'placeholder':'Enter A Number'
                            }))

    from_unit = forms.ChoiceField(choices = length_units, label = 'From', widget = forms.Select(attrs = {'class':'form-control'})
    )

    to_unit = forms.ChoiceField(choices = length_units, label = 'To', widget = forms.Select(attrs = {'class':'form-control'})
    )

class weight_conversion(forms.Form):
    weight_units = [
        ("mg", "Milligrams"),
        ("g", "Grams"),
        ("kg", "Kilograms"),
        ("oz", "Ounces"),
        ("lb", "Pounds"),
    ]

    value = forms.FloatField(label = 'Enter Value',
                            widget = forms.NumberInput(attrs = {
                                'class':'form-control',
                                'placeholder':'Enter A Number'
                            }))

    from_unit = forms.ChoiceField(choices = weight_units, label = 'From', widget = forms.Select(attrs = {'class':'form-control'})
    )

    to_unit = forms.ChoiceField(choices = weight_units, label = 'To', widget = forms.Select(attrs = {'class':'form-control'})
    )

class temperature_conversion(forms.Form):
    temperature_units = [
    ("C", "Celsius"),
    ("F", "Fahrenheit"),
    ("K", "Kelvin"),
    ]

    value = forms.FloatField(label = 'Enter Value',
                            widget = forms.NumberInput(attrs = {
                                'class':'form-control',
                                'placeholder':'Enter A Number'
                            }))

    from_unit = forms.ChoiceField(choices = temperature_units, label = 'From', widget = forms.Select(attrs = {'class':'form-control'})
    )

    to_unit = forms.ChoiceField(choices = temperature_units, label = 'To', widget = forms.Select(attrs = {'class':'form-control'})
    )

