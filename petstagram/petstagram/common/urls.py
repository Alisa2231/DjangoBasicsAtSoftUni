from django.urls import path
from petstagram.common import views

app_name = 'common'
urlpatterns = [
    path('', views.home_view, name='home'),
]