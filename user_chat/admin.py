# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class user_data_admin(admin.ModelAdmin):
	fields = ["user_email"]
	list_display = ["user_email"]
	list_display_links = ["user_email"]

	class Meta:
		model = user_data

admin.site.register(user_data, user_data_admin)
