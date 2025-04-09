from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django_api.views import CourseModelViewSet, CourseModelReadOnlyViewSet, obtain_jwt, refresh_jwt


router = DefaultRouter()
router.register('courses', CourseModelViewSet)
router.register('courses-readonly', CourseModelReadOnlyViewSet, basename='courses-readonly')

urlpatterns = [
    path('', include(router.urls)),
    path('obtain-jwt/', obtain_jwt, name='obtain-jwt'),
    path('refresh-jwt/', refresh_jwt, name='refresh-jwt'),
]