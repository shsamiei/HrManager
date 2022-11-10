from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
from pprint import pprint


# it is nested router way : 

router = routers.DefaultRouter()
router.register('Roles', views.RoleViewSet, basename='roles')
router.register('Employees', views.EmployeeProfileViewSet, basename='employees')



urlpatterns = router.urls 

