from django import forms


from .models import Audit

class AuditForm(forms.ModelForm):
    
    class Meta:
        model = Audit
        fields = "__all__"
