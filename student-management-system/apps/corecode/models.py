from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class SiteConfig(models.Model):
  """ Site Configurations """
  key = models.SlugField()
  value = models.CharField(max_length=200)

  def __str__(self):
    return self.key


class AcademicSession(models.Model):
  """ Academic Session """
  name = models.CharField(max_length=200, unique=True,verbose_name="Year")
  current = models.BooleanField(default=True)

  class Meta:
    ordering = ['-name']

  def __str__(self):
    return self.name


class AcademicTerm(models.Model):
  """ Academic Term """
  name = models.CharField(max_length=20, unique=True,verbose_name="Term")
  current = models.BooleanField(default=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class Subject(models.Model):
  """ Subject """
  name = models.CharField(max_length=200, unique=True,verbose_name="Subject")

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class StudentClass(models.Model):
  name = models.CharField(max_length=200, unique=True)
  class Meta:
    verbose_name = "Class"
    verbose_name_plural = "Class"
    ordering = ['name']

  def __str__(self):
    return self.name