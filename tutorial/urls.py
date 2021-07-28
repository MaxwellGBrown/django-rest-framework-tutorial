"""tutorial URL Configuration."""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(f"groups", views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),  # noqa

    path("snippets/", include("snippets.urls")),
]
