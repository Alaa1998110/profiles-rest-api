from django.urls import path
from . import views
from .views import HelloApiView

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
]