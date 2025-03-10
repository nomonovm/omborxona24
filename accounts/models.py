from django.contrib.auth.models import *
from main.models import Bolim


class Sotuvchi(models.Model):
    rasm = models.ImageField(upload_to="sotuvchilar/", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
