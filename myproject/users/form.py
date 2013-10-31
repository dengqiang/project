from  django import forms

class uploadform(forms.Form):
	imageform=forms.ImageField(required=False)
	

