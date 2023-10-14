from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_student/', views.add_student, name="add_student"),
    path('delete_student/<int:std_id>/', views.delete_student, name="delete_student"),
    path('update_student/<int:std_id>/', views.update_student, name="update_student"),
    path('do_update_student/<int:std_id>/', views.do_update_student, name="do_update_student"),
]

