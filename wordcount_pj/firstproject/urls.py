from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="home"),
    path('count/', wordcount.views.count, name="count"),
    path('result/', wordcount.views.result, name="result"),
]
