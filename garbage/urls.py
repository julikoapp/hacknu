from django.urls import path, include

from rest_framework.routers import DefaultRouter

from garbage import views

router = DefaultRouter()
router.register('client', views.ClientViewSet)
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.ClientLoginView.as_view()),
]
