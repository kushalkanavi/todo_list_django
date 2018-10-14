from django import forms 
from .models import task

class TaskinformForm(forms.ModelForm):
	class Meta:
		model=task
		
		fields = [
		'Title',
		'Description',
		'Due_Date',
		]

		labels = {
		'Title':'Title',
		'Description':'Description',
		'Due_Date':'Due_Date',
		}

		widgets = {
		'Title'			:forms.TextInput(attrs={'name':'eventname','class':'form-control','placeholder':'Title',}),
		'Description'	:forms.TextInput(attrs={'name':'eventdays','class':'form-control','placeholder':'Description'}),
		'Due_Date'		:forms.DateInput(attrs={'type':'date','name':'eventdate','class':'form-control','placeholder':'Due_Date'}),
		}
