from django.db import models
from django.contrib.auth.models import AbstractUser


class Administrator(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


#
# django User  == task Administrator
# Client       == task User
#

class Client(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    iban = models.CharField(max_length=34)
    created_by = models.ForeignKey(Administrator, on_delete=models.CASCADE)

