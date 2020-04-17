from __future__ import unicode_literals

import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

# ---- Base model ------

class CreatePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_date = models.DateTimeField('Postado', auto_now_add=True)
    set_date = models.DateTimeField('atualizado', auto_now=True)