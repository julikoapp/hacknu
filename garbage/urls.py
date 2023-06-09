from django.urls import path, include

from rest_framework.routers import DefaultRouter

from garbage import views

router = DefaultRouter()
router.register('client', views.ClientViewSet)
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.ClientLoginView.as_view()),
    path('tasks/', views.apiOverview, name="api-overview" ), # ????
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-delete/', views.taskDelete, name="task-delete"),
    path('task-filter-category/<str:pk>/', views.taskFilterCat, name="task-group"),
    path('task-filter-client/<str:pk>/', views.taskFilterClient, name="task-group"),
    path('task-filter-status/<str:pk>/', views.taskFilterStatus, name="task-group"),
]
