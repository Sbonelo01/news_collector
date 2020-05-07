from django.urls import path
from news.views import Scrape, news_list

urlpatterns = [
  path('scrape/', Scrape, name="scrape"),
  path('', news_list, name="home"),
]
