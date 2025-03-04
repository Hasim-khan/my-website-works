from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
# Create your models here.
class ContactData(models.Model):
    name = models.CharField(max_length=30, null = True)
    email = models.EmailField(max_length=40, null = False)
    contact = models.IntegerField(null = True)
    message = models.CharField(max_length=100, null = True)




class project_cms(models.Model):
    image = models.ImageField(upload_to = 'media', null=True)
    title = models.CharField(max_length=100, null = True, blank=False)
    pdate = models.DateTimeField(default=timezone.now)
    project_title = AutoSlugField(populate_from='title', unique=True, null=True, blank=False)


class blog_cms(models.Model):
    blog_image = models.ImageField(upload_to = 'media', null=True)
    blog_date = models.DateTimeField(default=timezone.now)
    blog_title = models.CharField(max_length=100, null = True, blank=False)
    blog_discription = models.CharField(max_length=600, null = False, blank=False)
    bloger_image = models.ImageField(upload_to = 'media', null= True)
    bloger_name = models.CharField(max_length=20, null=False, blank=False)
    blogs_title_slug = AutoSlugField(populate_from = 'blog_title', unique=True, null=True, blank=False)


# from django.core.exceptions import ValidationError
# from django.db import models
# import re

# class ContactData(models.Model):
#     name = models.CharField(max_length=30, null=True)
#     email = models.EmailField(max_length=40, null=False, unique=True)  # Enforcing unique email
#     contact = models.CharField(max_length=12, null=True)  # Change IntegerField to CharField to handle leading zeros and better validation
#     message = models.CharField(max_length=100, null=True)

#     def clean(self):
#         # Ensure contact is exactly 12 digits long
#         if self.contact:
#             if len(self.contact) != 12 or not self.contact.isdigit():
#                 raise ValidationError("Contact number must be exactly 12 digits.")

#         # Check if the email is already in use (Django's unique=True automatically handles this)
#         if not self._state.adding and ContactData.objects.filter(email=self.email).exists():
#             raise ValidationError(f"The email {self.email} is already registered.")

#         super().clean()

#     def save(self, *args, **kwargs):
#         # Run the clean method to ensure the validations are checked before saving the data
#         self.clean()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.name} - {self.email}"
