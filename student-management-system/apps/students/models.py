from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator, EmailValidator

from apps.corecode.models import StudentClass, Subject
import random

def random_string():
    return str(random.randint(21520000, 21529999))

class Student(models.Model):

    GENDER = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    
    id = models.CharField(default = random_string, max_length= 200, verbose_name= 'ID', primary_key= True)
    name = models.CharField(max_length=200,verbose_name= "Fullname")
    gender = models.CharField(max_length=10, choices=GENDER, default='male',verbose_name="gender")
    date_of_birth = models.DateField(default=timezone.now,verbose_name="birthday")
    current_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="class")
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    parent_mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True,verbose_name="parent phone number")
    email_regex=EmailValidator(message="Email is not valid")
    email=models.CharField(validators=[email_regex],max_length=30,default=None)
    address = models.TextField(blank=True,verbose_name="address")
    passport = models.ImageField(blank=True, upload_to='students/passports/',verbose_name="avatar")

    class Meta:
        ordering = ["name"]


    def __str__(self):
        return f'{self.name} )'

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True,verbose_name="Updated")
    csv_file = models.FileField(upload_to='students/bulkupload/')
