from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    product_dec = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'home/images', default="")


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    student_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=10)
    startup = models.CharField(max_length=100)


    def __str__(self):
        return self.username 

    