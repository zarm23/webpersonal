from django.urls import path
from . import views
from portfolio import views as portfolio_views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
]
