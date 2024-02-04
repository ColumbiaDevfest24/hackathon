# from django.db import models

# # Create your models here.
# class Event(models.Model):
#     date = models.DateField()
#     name = models.CharField(max_length = 100)

#     def __str__(self):
#         return self.name
    
# class UserProfile(models.Model):
#    def __init__(self,username):
#        self._username=username

#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username
