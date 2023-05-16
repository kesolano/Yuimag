from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),

    path('home/', views.home, name="home"),

    path('Users', views.Userss, name="Users"),

    path('Users_Registration', views.Users_Registration,
         name="Users_Registration"),

    path('Delete_User/<int:id>/', views.Delete_User,
         name="Delete_User"),

    path('Edit_User/<int:id>/', views.Edit_User, name="Edit_User"),

    path('Edit_list_user/<int:id>/', views.Edit_list_user, name="Edit_list_user"),

    path('gallery/', views.gallery, name='gallery'),

    path('viewPhoto/', views.viewPhoto, name="viewPhoto"),

    path('add/', views.addPhoto, name="add"),

    path('photo/<str:pk>/', views.viewPhoto, name="photo"),

    path('Delete_Image/<int:id>/', views.Delete_Image,
         name="Delete_Image"), 

    path('Delete_Category/<int:id>/', views.Delete_Category,
         name="Delete_Category"),
]
