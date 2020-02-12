from django import forms
from app.models import User, Package, Booking, Customer, Admin


class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"

class PackageForm(forms.ModelForm):
	Date=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"date"}))
	class Meta:
		model=Package
		fields="__all__"

class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields="__all__"


class BookingForm(forms.ModelForm):
	class Meta:
		model=Booking
		fields="__all__"

class AdminForm(forms.ModelForm):
	class Meta:
		model=Admin
		fields="__all__"