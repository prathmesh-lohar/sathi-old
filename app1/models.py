from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=50,default="", null=True, blank=True)
    age = models.CharField(max_length=50,default="0", null=True, blank=True)
    mobile = models.CharField(max_length=50,default="", null=True, blank=True)
    marrital_status = models.CharField(max_length=50,default="", null=True, blank=True)
    dob = models.CharField(max_length=50,default="", null=True, blank=True)
    height = models.CharField(max_length=50,default="", null=True, blank=True)
    color = models.CharField(max_length=50,default="", null=True, blank=True)
    Qualification = models.CharField(max_length=50,default="", null=True, blank=True)
    work = models.CharField(max_length=50,default="", null=True, blank=True)
    experience = models.CharField(max_length=50,default="", null=True, blank=True)
    hobbies = models.CharField(max_length=50,default="", null=True, blank=True)
    income = models.CharField(max_length=50,default="", null=True, blank=True)
    medical_condition = models.CharField(max_length=50,default="", null=True, blank=True)
    city = models.CharField(max_length=50,default="", null=True, blank=True)
    about_me = models.TextField(null=True,blank=True)

    is_featured = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

class family_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    father_name = models.CharField(max_length=50,default="", null=True, blank=True)
    
    father_education = models.CharField(max_length=50,default="", null=True, blank=True)
    father_occupation = models.CharField(max_length=50,default="", null=True, blank=True)
    mother_name = models.CharField(max_length=50,default="", null=True, blank=True)
    mother_education = models.CharField(max_length=50,default="", null=True, blank=True)
    mother_occupation = models.CharField(max_length=50,default="", null=True, blank=True)
    sister=models.TextField(null=True,blank=True)
    brother=models.TextField(null=True,blank=True)
    native_place=models.TextField(null=True,blank=True)
    relatives=models.TextField(null=True,blank=True)


    def __str__(self):
        return str(self.user)
    

class media(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dp = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)

    def __str__(self):
            return str(self.user)


    

