from django import forms
from .models import Country, Continent

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['continent'].queryset = Continent.objects.filter(is_active=True)