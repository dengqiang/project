#-*- coding:utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response
import myproject.settings as settings
from django.template import loader, RequestContext
from users.models import *
from users.form import *
import ImageFile
import os
# Create your views here.
def uploadimg(request):
	t=loader.get_template("upload.html")
	if request.method=='POST':
		form= uploadform(request.POST,request.FILES)
		if form.is_valid():
			f=request.FILES["pfile"]
			parser=ImageFile.Parser()
			for chunk in f.chunks():	
				parser.feed(chunk)
			img=parser.close()
			if not os.path.exists('/home/pic/'):
				os.mkdir('/home/pic/')
			path_name=os.path.join('/home/pic/',f.name)
			img.save(path_name)
			return HttpResponseRedirect("/login/")
	c=RequestContext(request,)
	return HttpResponse(t.render(c))
def newtrip(request):
	return render_to_response('new.html')
