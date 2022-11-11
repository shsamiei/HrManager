from rest_framework_nested import routers
from django.urls import path, include
from . import views



router = routers.DefaultRouter()
router.register('Roles', views.RoleViewSet, basename='roles')
router.register('Employees', views.EmployeeProfileViewSet, basename='employees')


employees_router = routers.NestedDefaultRouter(router, 'Employees', lookup='employee')
employees_router.register('salaries', views.SalaryViewSet, basename='employee-salaries')

urlpatterns = [
    path('accounts/create/<uuid:uid>/', views.EmployeeProfileCreateAPIView.as_view()),
    path('', include(router.urls)),
    path('', include(employees_router.urls)),
]

