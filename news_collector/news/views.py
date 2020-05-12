from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect
from news.models import Headline

# rendering requested data 
def scrape(request):
  return redirect("../")

# serving stored database objects
def news_list(request):
	headlines = Headline.objects.all()[::-1]	# reversing headlines to get the latest on top
	print(headlines)
	context = {
			'object_list': headlines,
	}

	return render(request, "news/index.html", context) # rendering database data
