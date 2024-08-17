from django import forms
from .models import CrudModel

class CrudForm(forms.ModelForm):
    class Meta:
     model = CrudModel
     fields = ['name','book','game']                                                                              
     widgets =  {'name':forms.TextInput(attrs={'class':'form-control'}),
                    'book':forms.TextInput(attrs={'class':'form-control'}),
                    'game':forms.TextInput(attrs={'class':'form-control'})}
        