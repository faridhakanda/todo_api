from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('todo_class/', views.TodoModelView.as_view()),
    path('todo_class/<int:pk>/', views.TodoModelView.as_view())
]