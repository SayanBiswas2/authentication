from django.db import models

# Create your models here.
class userinfo(models.Model):
  email= models.EmailField(max_length=60,unique=True)
  password = models.TextField()
  class Meta:
    db_table='user'