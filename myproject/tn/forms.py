from  django import forms

class loginform(forms.Form):
   	emailOrname = forms.CharField()
    	password = forms.CharField()
