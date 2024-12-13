from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path("", views.AddressAll.as_view()),
    path("<int:address_id>/", views.AddressUsers.as_view()),
    path("<int:user_id>/add", views.CreateUserAddress.as_view()),
    path("<int:address_id>/update", views.UpdateAddress.as_view()),
    path('<int:address_id>/delete', views.DeleteAddress.as_view()),
    path("getToken", obtain_auth_token),
    path("login/simpleJWT", TokenObtainPairView.as_view()),#코드 추가 부분
	path("login/simpleJWT/refresh", TokenRefreshView.as_view()),#코드 추가 부분
	path("login/simpleJWT/verify", TokenVerifyView.as_view())#코드 추가 부분
]


# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNTI3NjQ3OSwiaWF0IjoxNzM0MDY2ODc5LCJqdGkiOiJlNGY3NTkyNTJjMDY0MzkwODMzODEwZTQxNDM0MWMzMyIsInVzZXJfaWQiOjF9.OP90jjF2R1ZB5w_T_Wk0GuMWzkA-g4K1YUbNNIzV0HA",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0MDcwNDc5LCJpYXQiOjE3MzQwNjY4NzksImp0aSI6IjNiODI3NmFmNjZlNDQ4MGM4OGIwNWY3MDQ5MTdmMDc4IiwidXNlcl9pZCI6MX0.8qs_KZ6Hjh0yyaCM5eilPM6Xd9tF0LdndkNERnmUy8E"
# }