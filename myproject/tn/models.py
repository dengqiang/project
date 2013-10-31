from django.db import models

# Create your models here.
class User(models.Model):
	emailAddr=models.CharField(max_length=30)
	loginKey=models.CharField(max_length=15)
        loginName=models.CharField(max_length=30,primary_key=True)
	
