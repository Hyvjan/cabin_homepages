from django import forms
from homepages.models import Reservation

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):

	class Meta:
		model=Reservation
		fields=['arrival_date', 'end_date', 'first_name', 'last_name', 
		'email', 'phone_number', 'message']
		widgets = {
            'arrival_date': DateInput(),'end_date': DateInput(),
        }