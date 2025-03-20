from django import forms

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea) 
    email = forms.EmailField(help_text="email taak saalya",required=False)  

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 

# from Home.models import * 

# class LogForm(forms.ModelForm):
#     class meta:
#         model=Logger
#         fields='__all__'


from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        permissions = [('can_change_category','Can Change Category')]
        model = Booking
        fields = '__all__'