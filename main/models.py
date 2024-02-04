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
class OrganizationDataTable(models.Model):
    name = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200)
    address = models.CharField(max_length=200)
    contact_num = models.PositiveIntegerField()
    contact_email = models.EmailField(max_length=200)
    days = models.DateTimeField()
    
class OrganizationInfo:
    def __init__(self):
        self._name=''
        self._website_url=''
        self._address=''
        self._contact_num=''
        self._contact_email=''
        self._days=''
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
    def add_days(self,days):
        self._days=hours
