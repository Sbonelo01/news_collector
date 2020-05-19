import os
from django.shortcuts import render

# Create your views here.
import requests
import certifi
import urllib3
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

def scrape(request):
    session = requests.Session()
    session.headers = {
        "User-Agent": "Googlebot/2.1(+http://www.google.com/bot.html)"
    }
    url = "https://www.news24.com/"

    content = session.get(url, verify=True).content
    soup = BSoup(content, "html.parser")
    news = soup.find_all('div', {
        "class":"main_wrap"
    })

    for article in news:
        main = article.find_all('a')[0]
        link = main['href']
        image_src = str(main.find('img')['srcset']).split(" ")[-4]
        title = main['title']
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
    return redirect("../")


# serving stored database objects
def news_list(request):
	headlines = Headline.objects.filter()[::-1]	# reversing headlines to get the latest on top
	print(headlines)
	context = {
			'object_list': headlines,
	}

	return render(request, "news/index.html", context) # rendering database data























