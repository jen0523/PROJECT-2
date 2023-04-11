from django import forms
from .models import History
from .models import Historyin
from .models import Historyadd
from .models import Historyorder   


class PcOutForm(forms.ModelForm):

    class Meta:
        model= History
        fields= ('probe_card_id','tool_id', 'issue_by', 'user', 'comments',)

class PcInForm(forms.ModelForm):

    class Meta:
        model= Historyin
        fields= ('probe_card_id', 'technician', 'burned_needles', 'melted_needles', 'bent_needles', 
                 'phisical_issue', 'comments', 'probe_count_notes', 'action_taken', 'rework_sanding_cycles')
        
class PcInvForm(forms.ModelForm):

    class Meta:
        model= Historyadd
        fields= ('probe_card_id', 'vendor_name', 'vendor', 'arrived', 'vendor_serial', 'comments', 'status',)

class PcInvpoForm(forms.ModelForm):

    class Meta:
        model= Historyorder
        fields= ('po_number', 'probe_card_id', 'vendor_name', 'quantity', 'vendor', 'price', 'order_date',)