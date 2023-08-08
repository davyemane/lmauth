from django.db import models
from django.contrib.auth.models import User




class Langue(models.Model):
    id_langue = models.AutoField(null=False, primary_key=True)
    libelleLangue=models.TextField(null= False)
    def __str__(self):
        return self.libelleLangue 


class UserLangue(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    langue = models.ForeignKey (Langue, on_delete=models.CASCADE)
# Create your models here.
