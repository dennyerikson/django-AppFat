from django import forms
# from .models import Sats

# class SatsForm(forms.ModelForm):
#     class Meta:
#         model = Sats
#         filds = ('sats_quest_01')


CHOICES=[('select1','select 1'),
         ('select2','select 2')]

like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())