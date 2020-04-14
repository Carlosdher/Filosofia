from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

# ---- Base model ------

class CreatePost(models.Model):

    post_date = models.DateTimeField('Postado', auto_now_add=True)
    set_date = models.DateTimeField('atualizado', auto_now=True)


