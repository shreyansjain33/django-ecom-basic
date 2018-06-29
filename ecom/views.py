from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	context = {
		"title": "Home | Django Ecom",
		"heading": "This is the heading for the home page."
	}
	return render(request, "home.html", context)
