from django import forms
from .models import Booking
from django.forms import TextInput, Select, Textarea

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['name','email','phone','doctor','booked','time','desc']
        widgets = {
            'name':TextInput(attrs={
                "type":"text",
                "class":"form-control border-0",
                "placeholder":"Your Name",
                "style":"height: 55px;"
            }),
            'email':TextInput(attrs={
                "type":"email",
                "class":"form-control border-0",
                "placeholder":"Your Email",
                "style":"height: 55px;"
            }),
            'phone':TextInput(attrs={
                "type":"text",
                "class":"form-control border-0",
                "placeholder":"Your Phone",
                "style":"height: 55px;"
            }),
            'doctor':Select(attrs={
                "class":"form-control border-0",
                "style":"height: 55px; background-color:white"
            }),
            'booked':TextInput(attrs={
                "type":"date",
                "class":"form-control border-0",
                "style":"height: 55px;"
            }),
            'time':TextInput(attrs={
                "type":"time",
                "class":"form-control border-0",
                "style":"height: 55px;"
            }),
            'desc':Textarea(attrs={
                "type":"textara",
                "class":"form-control border-0",
                "placeholder":"Describe your problem",
                "rows":"5"
            })
        }