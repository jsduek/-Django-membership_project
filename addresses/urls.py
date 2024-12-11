from django.urls import path
from . import views

urlpatterns = [
    path("", views.AddressAll.as_view()),
    path("<int:address_id>/", views.AddressUsers.as_view()),
    path("<int:user_id>/add", views.CreateUserAddress.as_view()),
    path("<int:address_id>/update", views.UpdateAddress.as_view()),
    path('<int:address_id>/delete', views.DeleteAddress.as_view())
]