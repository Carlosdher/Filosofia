# -*- coding: utf-8 -*-
"""mysite URL 

[...]
"""


from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as core

app_name = 'core'

urlpatterns = [
    path('dashboard/', core.DashboardView.as_view(), name='dashboard')
]