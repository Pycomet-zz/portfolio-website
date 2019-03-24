from django import forms
from .models import Contact
from django.db import transaction

class HireForm(forms.ModelForm):
    """Hire me form"""

    class Meta:
        """Gives a nested space for inputing job request"""

        model = Contact
        fields = ['email', 'subject', 'message']



