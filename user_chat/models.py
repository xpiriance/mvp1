# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user_data(models.Model):
	user_email = models.CharField(max_length = 30, null = True, blank = True)

	def __unicode_(self):
		return unicode(self.user_email)