from django.urls import path
from . import handlers

urlpatterns = [
    path("register", handlers.register_handler),
    path("user-info", handlers.user_info_handler),
    path("users", handlers.users_handler),
    path("logout", handlers.logout_handler),
]
