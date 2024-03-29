from django.urls import path

from . import views, webhooks

app_name = "payment"
urlpatterns = [
    path("membership/", views.membership_list, name="membership_list"),
    path("process/", views.payment_process, name="payment_process"),
    path("completed/", views.completed, name="completed"),
    path("canceled/", views.canceled, name="canceled"),
    path("webhook/", webhooks.stripe_webhook, name="stripe_webhook"),
]
