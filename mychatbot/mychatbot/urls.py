
from django.contrib import admin
from django.urls import path

from chatbot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.process_text, name='process_text'),
    path('image', views.process_image, name='process_image'),
    path('report', views.report, name='report')
]
