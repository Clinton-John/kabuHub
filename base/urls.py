from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home , name="home"),
    path('home/', views.home , name="home"),
    path('signup/', views.signup , name="signup"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutPage , name="logout"),

    path('addEvent/', views.addEvent , name="add_event"),
    path('userProfile/<str:pk>/', views.userProfile , name="user_profile"),
    path('updateProfile/', views.updateProfile , name="update_profile"),

    path('deleteEvent/<str:pk>/', views.deleteEvent , name="delete_event"),
    path('deleteEvent/<str:pk>/', views.deleteUser , name="delete_user"),


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)