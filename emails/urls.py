from django.urls import include, path

from .views import email , fail_email

urlpatterns = [
    path('', email, name='email'),
    path('failed/applications', email, name='fail_email'),
] 