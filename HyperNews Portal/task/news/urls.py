from django.urls import path, re_path
from . import views      # importing all handlers from views.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.NewsPage.as_view(), name='NAME_OF_YOUR_VIEW'),
    path('create/', views.NewsCreate.as_view(), name='NAME_OF_YOUR_VIEW'),
    path('<news_link>/', views.NewsView.as_view(), name='NAME_OF_YOUR_VIEW')
]

urlpatterns += static(settings.STATIC_URL)
