from django.urls import path
from . import views
from django.contrib.syndication.views import Feed


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about_us_view, name='about-us'),
    path('contact-us/', views.contact_view, name='contact-us'),
    path('request-quote/', views.request_quote_view, name='request-quote'),
    path('company-history/', views.company_history_view, name='company-history'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
    path('services/', views.services_view, name='services'),
    path('teams/', views.teams_view, name='teams'),
    path('faqs/', views.faqs_view, name='faqs'),
    path('how-weather-can-impact-a-construction-project/', views.how_weather_view, name='how_weather_view'),
    path('how-to-choose-the-perfect-construction-company/', views.how_weather_view, name='how_choose_view'),
    path('portfolio/healthcare-facility/', views.healthcare_facility_view, name='healthcare_facility_view'),
    path('portfolio/Abattoir-Facility/', views.Abattoir_Facility_view, name='Abattoir_Facility_view'),
    path('portfolio/Development/', views.Development_view, name='Development_view'),
    path('portfolio/Infrastructure/', views.Infrastructure_view, name='Infrastructure_view'),
]
