from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views


urlpatterns = [
    ###Basic Website functionalities
    path('', views.home , name="home"),
    path('home/', views.home , name="home"),
    path('signup/', views.signup , name="signup"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutPage , name="logout"),

    #### The user profile and its functionalities
    path('userProfile/<str:pk>/', views.userProfile , name="user_profile"),
    path('updateProfile/', views.updateProfile , name="update_profile"),
    path('deleteUser/<str:pk>/', views.deleteUser , name="delete_user"),

    ### The Events section and related functionalities
    path('addEvent/', views.addEvent , name="add_event"),
    path('event/<str:pk>/', views.viewEvent , name="view_event"),
    path('updateEvent/<str:pk>/', views.updateEvent , name="update_event"),
    path('deleteEvent/<str:pk>/', views.deleteEvent , name="delete_event"),
    
    ##The sports Event section
    path('addSportsEvent/', views.addSportsEvent , name="add_sports_event"),
    path('sportEvent/<str:pk>/', views.viewSportEvent , name="view_sports_event"),
    path('updateSportsEvent/<str:pk>/', views.updateSportsEvent , name="update_sports_event"),
    path('deleteSportsEvent/<str:pk>/', views.deleteSportsEvent , name="delete_sports_event"),

    ##The Teams section
    path('addTeam/', views.addTeam , name="add_team"),
    path('leagueTable/', views.viewTable , name="league_table"),
    path('manageLeagueTable/', views.manageLeagueTable , name="manage_league_table"),
    path('updateTeam/<str:pk>/', views.updateTeam , name="update_team"),

    
    ### The Administrators Page
    path('adminsPage/', views.adminsPage ,  name="admins_page"),
    path('changeRole/', views.changeRole ,  name="change_role"),
    path('addSportsAdmin/', views.addSportsAdmin ,  name="add_sports_admin"),

      #email configuration and password reset section
    path('resetPassword/', auth_views.PasswordResetView.as_view(template_name='base/password_reset.html'), name="reset_password" ),
    path('resetPasswordSent/', auth_views.PasswordResetDoneView.as_view(template_name='base/password_reset_sent.html'),name="password_reset_done" ),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_form.html'), name="password_reset_confirm"),
    path('resetPasswordComplete/', auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_done.html'),name="password_reset_complete"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)