from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('info',views.info),
    path('review',views.review),
    path('about',views.about),
    path('look',views.look),



]