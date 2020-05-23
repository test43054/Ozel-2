from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    #path('addproduct/', views.addproduct, name='addproduct'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    path('myhomes/', views.myhomes, name='myhomes'),
    path('deletemyhomes/<int:id>', views.deletemyhomes, name='deletemyhomes'),
    path('update1/<int:id>', views.userhome_update, name='userhome_update'),



]