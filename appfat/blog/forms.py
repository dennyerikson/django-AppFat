from django import forms
from .models import Sats, Profile
from django.utils.safestring import mark_safe
from django.forms.widgets import RadioSelect

# class SatsForm(forms.ModelForm):
#     class Meta:
#         model = Sats
#         filds = ('sats_quest_01')

class SatsForm(forms.ModelForm):
    class Meta:
        model = Sats
        fields = ('sats_check', 'sats_quest_01')



class HorizontalRadioRenderer(RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     css_style = 'style="display: inline-block; margin-right: 10px;"'

    #     self.renderer.inner_html = '<li ' + css_style + '>{choice_value}{sub_widgets}</li>'


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
    ESCOLHA = forms.MultipleChoiceField(
        choices=CHOICES,
        required = True,
        widget=forms.RadioSelect(
            # renderer=HorizontalRadioRenderer
            attrs={
                'class' : 'myfieldclass'
                # 'style': 'display: inline-block; margin-right: 10px; margin-left: 10px; float: left;'
            }
        ),        
    )

