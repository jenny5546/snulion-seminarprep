from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'), # 추가
    path('<int:id>/edit', views.edit, name='edit'), 
    path('<int:id>/', views.show, name='show'), # 추가
    path('<int:id>/delete', views.delete, name='delete'), # 추가
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/like/', views.feed_like, name='like'),
    path('<int:pk>/follow/', views.follow_manager, name='follow'), #추가
]