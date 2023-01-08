from django import forms
from .models import Booking

SHIFTS = (
    ('1', 'morning'),
    ('2', 'afternoon'),
    ('3', 'evening'),
)
TIMING = (
    ('1', "9 to 2"),
    ('1', "2 to 6"),
    ('1', "6 to 10"),
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices = SHIFTS, help_text="select any one")
    time_tag = forms.ChoiceField(choices = TIMING)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"