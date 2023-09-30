
from django.urls import path
from movieapp import views
#Name Space
app_name = 'movieapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add', views.add,name='add'),
    path('update/<int:id>/', views.movie_edit, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
