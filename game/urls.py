
from django.urls import path
from django.urls import include
from game import views

urlpatterns = [
    path('ver1/',views.main),
    path('ver1/<str:name>/<int:id>/',views.game),
]