from django import forms
from .models import Sats, Profile
from django.utils.safestring import mark_safe

# class SatsForm(forms.ModelForm):
#     class Meta:
#         model = Sats
#         filds = ('sats_quest_01')

class SatsForm(forms.ModelForm):
    class Meta:
        model = Sats
        fields = ('sats_check', 'sats_quest_01')



class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

""" checkbox """
CHOICES = (
    ('0', '00'),
    ('1', '01'),
    ('2', '02'),
    ('3', '03'),
    ('4', '04'),
    ('5', '05'),
    ('6', '06'),
    ('7', '07'),
    ('8', '08'),
    ('9', '09'),
    ('10', '10'),
    #('valor', 'rotulo') widget checkbox
)
class SimpleForm(forms.Form):
   
    choice = forms.MultipleChoiceField(
    required=False,
    widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
    choices=CHOICES,
    )

