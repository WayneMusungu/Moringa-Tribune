# First we import the url function from the from the django.conf.urls.
from django.urls import path 

# We then import the app's views module.
from . import views

from django.conf import settings
from django.conf.urls.static import static


# We then import the app's views module.
urlpatterns=[
    # path('',views.welcome,name = 'welcome'),
    path('',views.news_today,name='newsToday'),
    path('archives/<past_date>/',views.past_days_news,name = 'pastNews'),
    path('search',views.search_results, name='search_results'),
    path('article/',views.article,name ='article')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)