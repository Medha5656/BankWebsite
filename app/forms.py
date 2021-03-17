from django import forms
from .models import Transaction

class transactionForm(forms.ModelForm):
	class Meta:
		model=Transaction
		fields=['trans_to','ammount']
