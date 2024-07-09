from django.urls import path
from .views import login_view, create_staff

urlpatterns = [
    path('login/', login_view, name='login'),
    path('create_staff/', create_staff, name='create_staff'),
    # other paths...
]