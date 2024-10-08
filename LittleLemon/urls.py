"""
URL configuration for LittleLemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from restaurant import views


schema_view = get_schema_view(
    openapi.Info(
        title="Little Lemon API",
        default_version='v1',
        description="ALittle Lemon is a web application for managing a restaurant's menu and table bookings. It provides APIs for performing CRUD operations on menu items and booking tables on specific dates. The application uses Django and Django REST Framework, with Djoser for user authentication and MySQL as the database backend.",
        contact=openapi.Contact(email="austineanyikwa@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('tables', views.BookingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
