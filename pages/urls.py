from django.urls import path

from .views import HomePageView as hp, AboutPageView as ab

urlpatterns = [
    path('about/', ab.as_view(), name='about'),
    path('', hp.as_view(), name='home'),

]