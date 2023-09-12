from django.urls import path

from .views import TestList, TestDetail

urlpatterns = [
    path("api/tests/", TestList.as_view()),
    path("api/tests/<int:pk>", TestDetail.as_view()),
]
