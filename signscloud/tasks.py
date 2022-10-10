from celery import shared_task
from django.contrib.auth import get_user_model

from django.core.mail import send_mail
from Api import settings

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Hecho"

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hola! Celery Test"
        message = "Aprovecha nuestras promociones"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Hecho"