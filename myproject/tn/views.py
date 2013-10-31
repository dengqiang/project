# Create your views here.
from django.http import * 
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from tn.models import User
from tn.forms import *
def UserRegister(request):
	errors=[0]*2
	t=loader.get_template("UserRegister.html")
	if request.method =='POST':
		addr=request.POST.get('form_email','')
		lname=request.POST.get('form_name','')
		
		if  User.objects.filter(emailAddr=addr):
			errors[0]="email has been registered!"
		if  User.objects.filter(loginName=lname):
			errors[1]="name has been existed!"
		if (errors[0]==0 and errors[1]==0):	
			user=User(emailAddr=request.POST.get('form_email',''),
				loginKey=request.POST.get('form_password',''),
				loginName=request.POST.get('form_name','')
				)
			user.save()
			return HttpResponseRedirect("/login/")

	c=RequestContext(request,{'email_errors':errors[0],'name_errors':errors[1]})
       	return HttpResponse(t.render(c))
 
def login(request):
	errors=[0]*2
	t=loader.get_template("login.html")
	if request.method== 'POST':
		form=loginform(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			if not User.objects.filter(emailAddr=cd['emailOrname']):
				errors[0]="email does not exist!"
			else:
				if User.objects.get(emailAddr=cd['emailOrname']).loginKey != cd ['password']:
					errors[1]="password is not correct!"
	
			if (errors[0]==0 and errors[1]==0):
				return HttpResponseRedirect("/UserRegister/")
	form=loginform()
	c=RequestContext(request,{'noName':errors[0],'pwderror':errors[1],'form':form})
	return HttpResponse(t.render(c))
	
def main(request):
	return render_to_response('main.html')
