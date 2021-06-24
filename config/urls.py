from django.contrib import admin
from django.urls import path, include
from player.views import PlayerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'players',PlayerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
