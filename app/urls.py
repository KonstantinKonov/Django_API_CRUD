from django.urls import path
from . import views

urlpatterns = [
    # list, create
    path('api/persons/', views.PersonCreateListAPIView.as_view()),
    # update, delete, read
    path('api/persons/<int:pk>/', views.PersonUpdateDeleteReadAPIView.as_view()),
]
