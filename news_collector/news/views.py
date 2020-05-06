from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

def Scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1(+http://www.google.com/bot.html)"}
  url = "https://https://www.theonion.com/"


content = session = session.get(url, verify=False).content
soup = BSoup(content, "html.parser")
News = soup.find_all('div', {"clas":"curation-module__item"})
for article in News:
    main = artcile.find_all('a')[0]
    link = main['href']
    image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main['title']
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.image = image_src
    new_headline.save()
  return redirect("../")

#served stored database objects
    def news_list(request):
        headlines = Headline.objects.all()[::-1]
        context = {
            'object_list': headlines,
        }
        return render(request, "news/home.html", context)
