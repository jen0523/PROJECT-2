from django import forms
from .models import History


class PcOutForm(forms.ModelForm):

    class Meta:
        model= History
        fields= ('probe_card_id','tool_id', 'user', 'comments',)