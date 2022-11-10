from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
from pprint import pprint


# it is nested router way : 

router = routers.DefaultRouter()
router.register('Roles', views.RoleViewSet, basename='roles')
router.register('Employees', views.EmployeeProfileViewSet, basename='employees')

employees_router = routers.NestedDefaultRouter(router, 'Employees', lookup='employee')
employees_router.register('salaries', views.SalaryViewSet, basename='employee-salaries')

urlpatterns = router.urls  + employees_router.urls

