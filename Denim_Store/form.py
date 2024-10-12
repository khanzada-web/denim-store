from django import forms

class Catagories(forms.Form):
    select_Catagories=[
        ('All',"All"),
        ('Male',"Male"),
        ('Female',"Female"),

    ]
    Catagory=forms.ChoiceField(choices=select_Catagories,widget=forms.RadioSelect(attrs={
        'class':'flex-col gap-10'
    }))