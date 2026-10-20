from django.urls import path

from common import views

app_name = 'common'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('redirect/', views.Redirect.as_view(), name='redirect'),
]