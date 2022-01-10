from django.urls import path,include
from . import views

from rest_framework import routers

from authapp.views import UserinfoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserinfoViewSet)



urlpatterns = [
	path('LoginV/', views.UserinfoViewSet.as_view({'get':'Email'}), name ='signin'),
	path('', include(router.urls)),
]





