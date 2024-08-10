from django.urls import path

from authentication.views import (
    authenticate
)
urlpatterns = [
    path("", authenticate, name="authenticate")
]