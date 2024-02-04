# from django.db import models

# # Create your models here.
# class Event(models.Model):
#     date = models.DateField()
#     name = models.CharField(max_length = 100)

#     def __str__(self):
#         return self.name
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add any additional user profile fields if needed

#     def __str__(self):
#         return self.user.username
#class Organization(models.Model):
    def __init__(self):
        self._name=''
        self._website_url=''
        self._address=''
        self._contact_num=''
        self._contact_email=''
        self._hours=''
    def add_username(self,name):
        self._name=name
    def add_website_url(self,website_url):
        self._website_url=website_url
    def add_address(self,address):
        self._address=address
    def add_contact_num(self,contact_num):
        self._contact_num=contact_num
    def add_contact_email(self,contact_email):
        self._contact_email=contact_email
    def add_hours(self,hours):
        self._hours=hours
