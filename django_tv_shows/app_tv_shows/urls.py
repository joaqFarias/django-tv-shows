from django.urls import path
from . import views, auth

urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/edit', views.edit),
]
