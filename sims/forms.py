from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyStudentsForm(UserCreationForm):
    class Meta:
        model = MyStudents
        fields = ['email', 'username']
        
class MyStaffForm(UserCreationForm):
    class Meta:
        model = MyStaff
        fields = ['email', 'username']
        
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
        
class PatientinfoForm(forms.ModelForm):
    Symptoms = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'Symptoms',
            'placeholder' : 'Write Symptoms',
        }))
    
    Problem = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'Problem',
            'placeholder' : 'Write Problem',
        }))
    
    Treatment = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'Treatment',
            'placeholder' : 'Write Treatment',
        }))
    
    Medicine = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'Medicine',
            'placeholder' : 'Write Medicine',
        }))
    class Meta:
        model = Patientinfo
        fields = ('Symptoms', 'Problem', 'Treatment', 'Medicine',)

        
class StaffContactinfoForm(ModelForm):
    class Meta:
        model = StaffContactinfo
        fields = '__all__'
