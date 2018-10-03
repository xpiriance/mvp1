from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from random import randint

from .models import *

# *********************************************************************************************************
'''
Section : In this section, I wrote functions for opening it
'''
# *********************************************************************************************************


def home_page(request):
	if request.user.is_authenticated():
		x = randint(0,1)
		if x==0:
			return HttpResponseRedirect("https://tawk.to/chat/5bb278af8a438d2b0cdfe78e/default")
		else:
			return HttpResponseRedirect("https://tawk.to/chat/5bb1dc358a438d2b0cdfe202/default")
		return render_to_response("chat_page.html")
	else:
		return render_to_response("index.html")

def login_data(request):
	# if request.method == "POST" and request.is_ajax():

	user_email = request.POST.get("user_email")
	user_password = request.POST.get("user_password")

	if user_data.objects.filter(user_email = user_email):
		pass
	else:
		query = user_data(user_email = user_email)
		query.save()

		# user = User.objects.get(email = user_email)
		# login(request, user)

	data = {
		"status" : 1,
	}
	return JsonResponse(data)