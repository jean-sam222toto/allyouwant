import site
from socket import fromshare

from django.contrib import admin
"""
from allyouwant.les_articles.models import Articles"""
from . models import *
admin.site.register(Articles)
