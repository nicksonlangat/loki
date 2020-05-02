from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def fail_email(request):
    subject = 'Decliened Application email  '
    message = """ 
Thank you for your interest in becoming an agent on our platform.
Unfortunately your application process has not met our criteria.
Please feel free to call us so we could discuss what steps could be taken to approve your application. """
  
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = ['ms@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    
    return HttpResponse("Email messages sent!", 200)
 
def email(request):
    subject = 'Approved Application Email '
    message = """ Congratulations! you are on your way to becoming a work from home agent on the arise platform.
Click not the link below and follow the instructions to complete your registration. 
After creating your profile you will reach the independent contractor section. 
Click on the join a call centre and add in our IB IDF number which will be provided below with the registration link.

                             www.ariseworkfromhome.com
                              IB IDF: 405349  """
  
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = ['ms@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    
    return HttpResponse("Email messages sent!", 200)