# apps/main/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewApi, TaskViewApi

# Создаем роутер для регистрации ViewSets
router = DefaultRouter()
router.register('users', UserViewApi, basename='user')
router.register('tasks', TaskViewApi, basename='task')

urlpatterns = [
    # Пути для регистрации, авторизации и обновления токенов
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Включаем все маршруты, сгенерированные роутером
    path('api/v1/', include(router.urls)),
]
