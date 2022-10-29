from django.urls import path
from django.conf.urls import include
from .views import *
from . import views

app_name = 'mainApp'

urlpatterns = [
path('loginapi/',LoginApi.as_view(), name='LoginApi'),
path('articles/<int:year>/', views.year_archive),
# path('articles/<int:year>/<int:month>/', views.month_archive),
# path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),

]