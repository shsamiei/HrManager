from rest_framework_nested import routers
from django.urls import path, include
from . import views



router = routers.DefaultRouter()
router.register('Roles', views.RoleViewSet, basename='roles')
router.register('Employees', views.EmployeeProfileViewSet, basename='employees')


# create_employee_router = routers.NestedDefaultRouter(router, 'Employees', lookup='employee')
# create_employee_router.register('create/<int:pk>', views.PostEmployeeProfileViewSet, basename='employee-pk')


employees_router = routers.NestedDefaultRouter(router, 'Employees', lookup='employee')
employees_router.register('salaries', views.SalaryViewSet, basename='employee-salaries')

# urlpatterns = router.urls  + employees_router.urls

urlpatterns = [
    path('accounts/create/<int:uid>/', views.EmployeeProfileCreateAPIView.as_view()),
    path('', include(router.urls)),
    path('', include(employees_router.urls)),


]
