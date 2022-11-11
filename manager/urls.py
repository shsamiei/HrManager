from rest_framework_nested import routers
from . import views



router = routers.DefaultRouter()
router.register('Roles', views.RoleViewSet, basename='roles')
router.register('Employees', views.EmployeeProfileViewSet, basename='employees')

employees_router = routers.NestedDefaultRouter(router, 'Employees', lookup='employee')
employees_router.register('salaries', views.SalaryViewSet, basename='employee-salaries')

urlpatterns = router.urls  + employees_router.urls

