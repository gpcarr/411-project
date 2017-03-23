# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:38:58 2017

@author: Allison Kaufman


OWMapp urls
"""

from django.conf.urls import url

from OWMapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^weather/$', views.weather, name='weather'),
]