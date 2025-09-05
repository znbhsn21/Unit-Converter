from django import forms

class length_conversion(forms.Form):
    length_units = [
        ('km':'Kilometer'),
        ('m':'Meter'),
        ('cm':'Centimeter'),
        ('mm':'Millimeter'),
        ('mi':'Miles'),
        ('yd':'Yards'),
        ('ft':'Feet'),
        ('in':'Inches'),
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