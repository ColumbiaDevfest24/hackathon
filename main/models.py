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