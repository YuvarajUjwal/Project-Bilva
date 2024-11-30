from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('about/',views.About,name='about'),
    path('gallery/',views.Gallery,name='gallery'),
    path('enquire-us/',views.Contact,name='contact'),
    path('services/',views.Services,name='services'),
    path('adminpage/',views.Options,name='adminpage'),
    path('Update-tag/<int:pk>/',views.Update_tag,name='update_tag'),
    path('delete-content/<int:pk>/',views.Delete_content,name='delete_content'),
    path('image_check/',views.ImageShow,name='image_check'),
    path('upload/',views.upload_image,name='upload'),
    path('db/',views.Enquire_db,name='db'),
    path('create_tag/',views.Create_tag,name='create_tag'),
    path('office/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('gallery/<str:slug>/',views.category,name='category'),
    path('delete-image/<int:pk>/',views.Delete_image,name='delete_image'),
]