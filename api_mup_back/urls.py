from django.contrib import admin
from django.urls import path
from mup_back.views import AboutViewSet, BoletimViewSet, GeneralViewSet, post_about, post_boletim, post_general 
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'about', AboutViewSet, basename='about')
router.register(r'boletim', BoletimViewSet, basename='boletim')
router.register(r'general', GeneralViewSet, basename='general')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('post_about/', post_about),
    path('post_boletim/', post_boletim),
    path('post_general/', post_general),
]
