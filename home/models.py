from django.db import models
from datetime import datetime, date

# Create your models here.
actions = (
    ('done','DONE'),
    ('not done','NOT DONE'),
    ('read', 'READ'),
    ('not read', 'Not Read'),
    ('problem solved','PROBLEM SOLVED'),
)

couns = (
    ('not seen','NOT SEEN'),
    ('solved','SOLVED'),
    ('seen bot not contected','SEEN BUT NOT CONTECTED'),
    ('on hold', 'ON HOLD'),
)

class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    content = models.TextField()
    actionss = models.CharField(max_length=200, choices=actions, default='not read')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' -- STATUS -->> ' + self.actionss

class Counselling(models.Model):
    fname1 = models.CharField(max_length=200)
    lname1 = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=15)
    email1 = models.CharField(max_length=50)
    content1 = models.TextField()
    modes = models.CharField(max_length=100)
    couns = models.CharField(max_length=200, choices=actions, default='not seen')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.fname1 + ' ' + self.lname1 + '----------->' + self.couns

class faq(models.Model):
    que = models.CharField(max_length=500)
    lans = models.TextField()

    def __str__(self):
        return self.que