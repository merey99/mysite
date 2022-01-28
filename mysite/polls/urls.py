from django.urls import path
from .views import Login, Registration, TaskToDoList, TaskToDoListCreate, TaskToDoListDelete, TaskToDoListDetail, TaskToDoListUpdate
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskToDoList.as_view(), name='tasks'),
    path('tasks-create/', TaskToDoListCreate.as_view(), name='tasks-create'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Registration.as_view(), name='register'),
    path('tasks/<int:pk>/', TaskToDoListDetail.as_view(), name='tasks-detail'),
    path('tasks-update/<int:pk>/',
         TaskToDoListUpdate.as_view(), name='tasks-update'),
    path('tasks-delete/<int:pk>/', TaskToDoListDelete.as_view(), name='tasks-delete')
]
