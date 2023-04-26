from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),

    path('home', views.home, name="home"),

    path('Users', views.Userss,
         name="Users"),

    path('login/', views.loginUser, name="login"),

    path('logout/', views.logoutUser, name="logout"),
    
    path('register/', views.registerUser, name="register"),

    path('Users_Registration', views.Users_Registration,
         name="Users_Registration"),

    path('Delete/<username>', views.Delete_User,
         name="Delete"),

    path('Edit_User/<username>', views.Edit_User, name="Edit_User"),

    path('Edit_list_user/', views.Edit_list_user),

    path('gallery/', views.gallery, name='gallery'), 

    path('viewPhoto/', views.viewPhoto, name="viewPhoto"),

    path('add/', views.addPhoto, name="add"),

    path('photo/<str:pk>/', views.viewPhoto, name="photo"),

    
]
