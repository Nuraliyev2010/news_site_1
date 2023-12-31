from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_view, name="index_url"),
    path('news/', news_view, name="news_urls"),
    path('service/', service_view, name="service_urls"),
    path('recipes/', recipes_view, name="recipes_urls"),
    path('search/', search_view, name="search_url"),
    path('logout/', logout_view, name="logout_url"),
    path('', login_view, name="login_url"),
    path('log-up/', signup_view, name="signup_url"),
    path('about/', about_view, name="about_url"),
    path('update-deatil/<int:pk>/', update_blog_view, name="update_blog_url"),
    path('delete-deatil/<int:pk>/', delete_blog_view, name="delete_blog_url"),
    path('blog-deatil/<int:pk>/', single_view, name="single_url"),
    path('profile/', profile_view, name="profile_url"),
    path('delete_user/<int:pk>/', delete_user_view, name="delete_user_url"),
]
