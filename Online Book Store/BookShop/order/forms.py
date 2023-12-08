from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		("Andhra Pradesh","Andhra Pradesh"),
                         ("Arunachal Pradesh ","Arunachal Pradesh "),
                         ("Assam","Assam"),
                         ("Bihar","Bihar"),
                         ("Chhattisgarh","Chhattisgarh"),
                         ("Goa","Goa"),("Gujarat","Gujarat"),
                         ("Haryana","Haryana"),
                         ("Himachal Pradesh","Himachal Pradesh"),
                         ("Jammu and Kashmir ","Jammu and Kashmir "),
                         ("Jharkhand","Jharkhand"),
                         ("Karnataka","Karnataka"),
                         ("Kerala","Kerala"),
                         ("Madhya Pradesh","Madhya Pradesh"),
                         ("Maharashtra","Maharashtra"),
                         ("Manipur","Manipur"),
                         ("Meghalaya","Meghalaya"),
                         ("Mizoram","Mizoram"),
                         ("Nagaland","Nagaland"),
                         ("Odisha","Odisha"),
                         ("Punjab","Punjab"),
                         ("Rajasthan","Rajasthan"),
                         ("Sikkim","Sikkim"),
                         ("Tamil Nadu","Tamil Nadu"),
                         ("Telangana","Telangana"),
                         ("Tripura","Tripura"),
                         ("Uttar Pradesh","Uttar Pradesh"),
                         ("Uttarakhand","Uttarakhand"),
                         ("West Bengal","West Bengal"))

	DISCRICT_CHOICES = (
                ("Mumbai","Mumbai"),
                ("Delhi","Delhi"),
                ("Bangalore","Bangalore"),
                ("Hyderabad","Hyderabad"),
                ("Ahmedabad","Ahmedabad"),
                ("Chennai","Chennai"),
                ("Kolkata","Kolkata"),
                ("Pune","Pune"),
                ("Surat","Surat"),
                ("Jaipur","Jaipur"),
                ("Lucknow","Lucknow"),
                ("Kanpur","Kanpur"),
                ("Nagpur","Nagpur"),
                ("Visakhapatnam","Visakhapatnam"),
                ("Thane","Thane"),
                ("Bhopal","Bhopal"),
                ("Ludhiana","Ludhiana"),
                ("Agra","Agra"),
                ("Nashik","Nashik"),
                ("Vadodara","Vadodara"),
                ("Patna","Patna"),
                ("Ghaziabad","Ghaziabad"),
                ("Rajkot","Rajkot"),
                ("Meerut","Meerut"),
                ("Amritsar","Amritsar"),
                ("Varanasi","Varanasi"),
                ("Srinagar","Srinagar"),
                ("Aurangabad","Aurangabad"),
                ("Dhanbad","Dhanbad"),
                ("Solapur","Solapur"),
                ("Jodhpur","Jodhpur"),
                ("Madurai","Madurai"),
                ("Tiruchirappalli","Tiruchirappalli"))
            

	PAYMENT_METHOD_CHOICES = (
		('paypal', 'paypal'),
		('net banking','net banking')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'pin_code', 'payment_method', 'account_no', 'transaction_id']
