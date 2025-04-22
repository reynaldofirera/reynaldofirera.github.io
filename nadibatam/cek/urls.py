from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # atau pola URL lainnya
]
