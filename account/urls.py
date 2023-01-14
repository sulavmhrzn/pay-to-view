from django.urls import include, path

from . import views

app_name = "account"
urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", include("django.contrib.auth.urls")),
]
