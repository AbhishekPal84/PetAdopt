from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # ✅ THIS LINE FIXES EVERYTHING
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/',views.login,name = 'login'),
     path('signup/',views.signup,name = 'signup'),
]