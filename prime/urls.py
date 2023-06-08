from django.urls import path
from .views import GetAllUser

urlpatterns = [
    path('api/get-access-token/<int:pk>', GetAllUser.as_view(), name='get_access_token'),
]
