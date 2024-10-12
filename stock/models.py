from django.db import models

class item(models.Model):
    CATEGORY_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    icon_Image=models.FileField(upload_to="media", max_length=100)
    catagory=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    Name=models.CharField(max_length=100)
    price=models.CharField(max_length=50)
